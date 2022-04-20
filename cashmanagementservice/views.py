from django.core.exceptions     import ObjectDoesNotExist 
from django.db                  import transaction
from django.db.utils            import DatabaseError
from users.models               import User
from bank.models                import AccountHolder
from .models                    import Send,Send_detail
from .serializers               import SendMoneySerializer, SendMemoSerializer, SendMoneyListSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework             import serializers
from rest_framework.generics    import CreateAPIView


class SendMoneyView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SendMoneySerializer
    @transaction.atomic(using='default')
    def post(self, request):
        try:
            with transaction.atomic():
                data = request.data
                serializer = self.get_serializer(data=data)
                user_id = request.session.get('user')
                
                if not user_id == True:
                    raise serializers.ValidationError("INVALID_SESSION_USER")
                
                if serializer.is_valid(raise_exception=True):
                    user = User.objects.get(identification=request.user)
                    user.point = user.point - request.data['amount'] - request.data['fee']
                
                    serializer.save()
                    user.save() 
                    send_first = Send.objects.latest("id").id
                   
                    if AccountHolder.objects.get(account_number=request.data['account_no']):
                        recipient = AccountHolder.objects.get(account_number=request.data['account_no'])
                        recipient.deposit =  recipient.deposit + request.data['amount'] 
                        recipient.save()
                        
                        request.session.flush()
                        
                        return Response({"data":serializer.data,"current_send":send_first,"user_point":user.point}, status=201)
                else:   
                    return Response(serializer.errors,status=404)
         
        except DatabaseError:
            raise serializers.ValidationError("DEPOSIT_ZERO")
        
        except ObjectDoesNotExist:
            raise serializers.ValidationError("DOSENOT_EXIST")



class SendMemoView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        data = request.data
        serializer = SendMemoSerializer(data=data)
        send_id    = Send.objects.get(id=data["send"])
        if serializer.is_valid(raise_exception=True):
            send = Send_detail.objects.create(
            memo = request.data['memo'],
            send = send_id
        )       
            send.save()
             
            return Response(data=serializer.data, status=201)
        
    def get_send(self,pk):
        try:
            send = Send.objects.get(id=pk)
            return send
        
        except Send.DoesNotExist:
            return None
      
    def get(self, request, pk):
        send       = self.get_send(pk)
        user_point = request.user.point  
        user_card  = request.user.card_number
        
        if send is not None:
            serializer = SendMoneyListSerializer(send)
            results ={
                "send_data"  : serializer.data,
                "user_point" : user_point,
                "user_card"  : user_card
            }
            
            return Response(results,status=200)
        else:
            return Response(status=400)

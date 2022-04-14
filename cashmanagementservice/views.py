from django.core.exceptions     import ObjectDoesNotExist 
from django.db                  import transaction
from django.db.utils            import DatabaseError
from users.models               import User
from bank.models                import AccountHolder
from .models                    import Send
from .serializers               import SendMoneySerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework             import serializers
from rest_framework.generics    import CreateAPIView


class SendMoneyView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SendMoneySerializer
    @transaction.atomic(using='default')
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                data = request.data
                serializer = self.get_serializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    user = User.objects.get(identification=request.user)
                    user.point = user.point - request.data['amount'] - request.data['fee']
                

                    serializer.save()
                    user.save() 
                    send_first =Send.objects.latest("id").id
                    print(send_first)
                    if AccountHolder.objects.get(account_number=request.data['account_no']):
                        recipient = AccountHolder.objects.get(account_number=request.data['account_no'])
                        recipient.deposit =  recipient.deposit + request.data['amount'] 
                        recipient.save()
                     
                        return Response({"data":serializer.data,"current_send":send_first}, status=201)
                
                else:   
                    return Response(serializer.errors,status=404)
                
      
        
        except DatabaseError:
            raise serializers.ValidationError("잔액이 부족합니다.")
        
        except ObjectDoesNotExist:
            raise serializers.ValidationError("존재 하지 않는 계좌입니다.")


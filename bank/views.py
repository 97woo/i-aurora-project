from rest_framework.views       import APIView
from .serializer                import AccountCheckSerializer
from rest_framework import serializers
from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated
from bank.models import AccountHolder


class AccountCheckView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        try:
           
            lookup_field = "name"
            serializer = AccountCheckSerializer(
            data=  {
                    "bank"           : request.data['bank'],
                    "account_number" : request.data['account_number'],
                    "name"           : lookup_field
                    })
            
            if serializer.is_valid(raise_exception=True):
                return Response(serializer.data,status=200)
            else:
                return Response(serializer.errors, status=400)
        
        except KeyError:
            raise serializers.ValidationError("KEY_ERROR")
        
        except AccountHolder.DoesNotExist:
              raise serializers.ValidationError("INVAILD_ACCOUNTNUMBER")
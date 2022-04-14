from .models        import Send
from users.models   import User

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response                 import Response
from rest_framework.generics                import CreateAPIView
from rest_framework import serializers





class SendMoneySerializer(serializers.ModelSerializer):
    def create(self, validated_data,):
        send=Send.objects.create(
            amount      = validated_data['amount'],
            account_no  = validated_data['account_no'],
            fee         = validated_data['fee'],
            remittor    = validated_data['remittor'],
            recipient   = validated_data['recipient'],
            bank_name   = validated_data['bank_name'],
            bankcode    = validated_data['bankcode'],
            user        = self.context['request'].user
         ) 
        return send

    class Meta:
        model = Send
        fields =['amount','fee','remittor','recipient','account_no','bank_name','bankcode']
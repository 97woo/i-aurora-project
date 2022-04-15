from .models        import Send
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

class SendMemoSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
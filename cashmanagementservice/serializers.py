from rest_framework import serializers
from .models        import Send


class SendMoneySerializer(serializers.ModelSerializer):
#     def create(self, data):
#         send = Send.objects.create(
#             "amount"     : data['amount'],
#             "account_no" : data['account_no'],
#             "fee"        : data['fee'],
#             "remittor"   : data['remittor'],
#             "recipient"  : data['recipient'],
#             "bank_name"  : data['bank_name'],
#             "user"       : data['user']
#         )
#         send.save()
#         return send
    
    class Meta:
        model = Send
        fields =['amount','fee','remittor','recipient','account_no','bank_name','user']
        
        
    
    
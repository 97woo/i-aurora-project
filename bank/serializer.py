from rest_framework import serializers
from .models        import Bank, AccountHolder
from django.core.exceptions import ObjectDoesNotExist

class AccountCheckSerializer(serializers.ModelSerializer):
    def validate(self, data):
        name = serializers.CharField(read_only=True)
        try:
           
            account_number = data.get("account_number")
            bank           = data.get('bank')
            account        = AccountHolder.objects.get(account_number=account_number)
            name           = account.name
            
            if not Bank.objects.filter(id=bank.id).exists():
                raise serializers.ValidationError("존재하지 않는 은행입니다.")
            
            if not AccountHolder.objects.filter(account_number=account_number,bank_id=bank.id).exists():
                raise serializers.ValidationError("입력한 계좌번호가 존재하지 않아요. 계좌번호를 다시 확인해주세요")

            data = {
                "account_number" : account_number,
                "bank"           : bank,
                "name"           : name,
            }
            return data
        
       
        except ObjectDoesNotExist:
            raise serializers.ValidationError("계좌가 존재하지 않습니다.")
    class Meta:
        model  = AccountHolder
        fields =['bank', 'account_number','name'] 
        
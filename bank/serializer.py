from rest_framework import serializers
from .models        import Bank, AccountHolder


class AccountCheckSerializer(serializers.ModelSerializer):
    def validate(self, data):
            account_number = data.get("account_number")
            bank           = data.get('bank')
            account        = AccountHolder.objects.get(account_number=account_number)
            name           = account.name
            
            if not AccountHolder.objects.filter(account_number=account_number).exists():
                    raise serializers.ValidationError("INVALID_ACCOUNTNUMBER")

            if not AccountHolder.objects.filter(account_number=account_number,bank_id=bank.id).exists():
                raise serializers.ValidationError("INVALID_ACCOUNTNUMBER")

            data = {
                "account_number" : account_number,
                "bank"           : bank,
                "name"           : name,
            }
            
            return data
    class Meta:
        model  = AccountHolder
        fields =['bank', 'account_number','name'] 
        
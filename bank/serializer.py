from rest_framework import serializers
from .models        import Bank, AccountHolder
from .validators    import validate_account_kb, validate_account_ibk, validate_account_sh, validate_account_nh
from django.db      import models
from rest_framework.validators import UniqueTogetherValidator

class AccountCheckSerializer(serializers.ModelSerializer):
    def validate(self, data):
        
        try:
            acccount_number = data.get("account_number")
            bank            = data.get('bank')
    
            if not Bank.objects.filter(id=bank.id).exists():
                raise serializers.ValidationError("존재하지 않는 은행입니다.")
            
            if not AccountHolder.objects.filter(account_number=acccount_number,bank_id=bank.id).exists():
                raise serializers.ValidationError("존재하지 않는 계좌입니다. 은행과 계좌번호를 확인해주세요")
            
            
            return data
        
       
        except Bank.DoesNotExist:
            return serializers.ValidationError("은행이 존재하지 않습니다.")
    class Meta:
        model  = AccountHolder
        fields =['bank', 'account_number'] 
        
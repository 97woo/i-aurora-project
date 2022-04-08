from rest_framework import serializers
from .models        import Bank, AccountHolder
from .validators    import validate_account_kb, validate_account_ibk, validate_account_sh, validate_account_nh
from django.db      import models

class AccountCheckSerializer(serializers.ModelSerializer):
    
    account_number = serializers.CharField(max_length=300)
    bank           = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    def validate(self, data):
        print(data)
        try:
            if data.get('bank') == "국민":
                if not validate_account_kb(data['account_number']):
                    raise serializers.ValidationError('올바른 계좌번호가 아닙니다.')
                
                if not AccountHolder.objects.filter(account_number=data['account_number']):
                        raise serializers.ValidationError('존재하는 계좌번호가 아닙니다.')
                
                
            elif data.get('bank') == "신한":
                if not validate_account_sh(data['account_number']):
                    raise serializers.ValidationError('올바른 계좌번호가 아닙니다.')
                  
                if not AccountHolder.objects.filter(account_number=data['account_number']):
                    raise serializers.ValidationError('존재하는 계좌번호가 아닙니다.')
                    
            elif data.get('bank') == "농협":
                if not validate_account_nh(data['account_number']):
                    raise serializers.ValidationError('올바른 계좌번호가 아닙니다.')
                    
                if not AccountHolder.objects.filter(account_number=data['account_number']):
                    raise serializers.ValidationError('존재하는 계좌번호가 아닙니다.')
                    
            elif data.get('bank') == "기업":
                if not validate_account_ibk(data['account_number']):
                    raise serializers.ValidationError('올바른 계좌번호가 아닙니다.')
                    
                if not AccountHolder.objects.filter(account_number=data['account_number']):
                    raise serializers.ValidationError('존재하는 계좌번호가 아닙니다.')
                    
    
           
            account_holder = AccountHolder.objects.get(account_number=data['account_number'])
            account_holder.name
            return data,  account_holder.name
        
        except AccountHolder.DoesNotExist:
            raise serializers.ValidationError("계좌번호가 존재하지 않습니다.")
    
    class Meta:
        model = AccountHolder
        fields =['account_number','bank']
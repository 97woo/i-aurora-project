from rest_framework import serializers
from .models        import User
from .validators    import validate_identification , validate_password
from aurora.settings import aurora_settings

JWT_PAYLOAD_HANDLER = aurora_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = aurora_settings.JWT_ENCODE_HANDLER


class UserIDSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not validate_identification(data['identification']):
            raise serializers.ValidationError('영문과 숫자로 6자리이상 20자리미만으로 입력해주세요!')
        return data
    
    class Meta:
        model = User
        fields =['identification']

class UserSignUpSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not validate_password(data['password']):
            raise serializers.ValidationError('숫자만으로 6자리를 입력해주세요!')
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
        identification= validated_data['identification'],
        password   = validated_data['password'],
        point      = self
        )
        user.save()
        return user
    
    class Meta:
        model = User
        fields =['identification', 'password','point']
        extra_kwargs = {'password': {'write_only': True}}



class UserSignInSerializer(serializers.Serializer):
    identification = serializers.CharField(max_length=100)
    password       = serializers.CharField(max_length=50, write_only=True)
        
    def validate(self, data):
        identification = data.get("identification")

        try:
            user = User.objects.get(identification=identification)      
            data['user'] = user
            
            if not validate_password(data['password']):
                raise serializers.ValidationError('숫자만으로 6자리를 입력해주세요!')
            
            return data
        
        except User.DoesNotExist:
            raise serializers.ValidationError("사용자가 존재하지 않습니다.")
    class Meta:
        model = User
        fields =['identification','password']
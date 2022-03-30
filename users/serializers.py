from rest_framework import serializers
from .models        import User
from .validators import validate_password

class UserSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not validate_password(data['trinity_password']):
            raise serializers.ValidationError('숫자만으로 6자리를 입력해주세요!')
        return data
    
    class Meta:
        model = User
        fields =['trinity_id', 'trinity_password', 'point']
        extra_kwargs = {'trinity_password': {'write_only': True}}
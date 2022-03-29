from rest_framework import serializers
from .models        import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['trinity_id', 'trinity_password', 'point']
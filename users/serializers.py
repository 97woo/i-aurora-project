from xml.dom.minidom import Identified
from rest_framework import serializers
from .models        import User
from .validators    import validate_identification , validate_password
from rest_framework_simplejwt.tokens import RefreshToken



class UserIDSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not validate_identification(data['identification']):
            raise serializers.ValidationError('INVALID_ID')
        return data
    
    class Meta:
        model = User
        fields =['identification']

class UserSignUpSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not validate_password(data['password']):
            raise serializers.ValidationError('INVALID_PASSWORD')
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            identification = validated_data['identification'],
            password       = validated_data['password'],
            point          = self,
            card_number    = self,
        )
        user.save()
        return user
    
    class Meta:
        model = User
        fields =['identification', 'password','point','card_number']
        extra_kwargs = {'password': {'write_only': True}}



class UserSignInSerializer(serializers.ModelSerializer):
    identification = serializers.CharField(max_length=100)
    password       = serializers.CharField(max_length=50, write_only=True)
        
    def validate(self, data):
        identification = data.get("identification")
        password       = data.get('password')
        
        try:
            user = User.objects.get(identification=identification)      
            data['user'] = user
            
            if not user.check_password(password):
                raise serializers.ValidationError('INVALID_PASSWORD')
            
            token   = RefreshToken.for_user(user)
            refresh = str(token)
            access  = str(token.access_token)
            
            data ={
                'user'    : user,
                'refresh' : refresh,
                'access'  : access
            }
            return data
        
        except User.DoesNotExist:
            raise serializers.ValidationError("NONEXISTENT_USER")
    
    class Meta:
        model = User
        fields =['identification','password']
        
        
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['point','card_number']
        

class UserPasswordSerializer(serializers.ModelSerializer):
   
    try:    
        def validate(self, data):
            user     = self.context['request'].user
            password = data['password']
            
            if not user.check_password(password):
                raise serializers.ValidationError('INVALID_PASSWORD')
                 
            return data
          
    
    except User.DoesNotExist:       
       raise serializers.ValidationError("NONEXISTENT_USER")
    
    class Meta:
        model = User
        fields =['password']
        extra_kwargs = {'password': {'write_only': True}}



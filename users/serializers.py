from xml.dom.minidom import Identified
from rest_framework import serializers
from .models        import User
from .validators    import validate_identification , validate_password
from rest_framework_simplejwt.tokens import RefreshToken



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
                raise serializers.ValidationError('올바른 패스워드를 입력해주세요')
            
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
            raise serializers.ValidationError("사용자가 존재하지 않습니다.")
    
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
            session  = self.context['request'].session
            if not user.check_password(password):
                raise serializers.ValidationError('올바른 패스워드를 입력해주세요')
            
            if User.objects.get(id=user.id):
                session['user_id'] = user.id
                print(session['user_id'])
                
            return data
          
    
    except User.DoesNotExist:       
       raise serializers.ValidationError("사용자가 존재하지 않습니다.")
    
    class Meta:
        model = User
        fields =['password']
        extra_kwargs = {'password': {'write_only': True}}



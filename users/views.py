from django.http                     import JsonResponse

from rest_framework.views            import APIView
from rest_framework.decorators       import api_view
from rest_framework.permissions      import IsAuthenticated
from rest_framework.response         import Response
from rest_framework.generics         import CreateAPIView
from .serializers                    import UserSignUpSerializer, UserIDSerializer, UserSignInSerializer
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def id_check(request):
    permission_classes = [IsAuthenticated]
    if request.method == 'POST':
        serializer = UserIDSerializer(data=request.data)
        
        if serializer.is_valid():
            return JsonResponse(serializer.data,status=200)
        else:
            return Response(serializer.errors, status=400)
    return JsonResponse(serializer.data, status=201)
    
class SignUpView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = UserSignUpSerializer
        
        if serializer.is_valid(raise_exception=False):
             user =serializer.save(request)
             token =RefreshToken.for_user(user)
             refresh = str(token)
             access = str(token.access_token)
            
        return JsonResponse ({ 
                 'user'   : user,
                 'access' : access,
                 'refresh': refresh
              })

class SignInView(APIView):
       
    def post(self, request):
        
        serializer = UserSignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
           
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({'token': token.key})
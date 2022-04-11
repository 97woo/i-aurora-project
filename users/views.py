from django.http                     import JsonResponse

from rest_framework.views       import APIView
from rest_framework.decorators  import api_view 
from rest_framework.response    import Response
from rest_framework.generics    import CreateAPIView
from .serializers               import UserInfoSerializer, UserSignUpSerializer, UserIDSerializer, UserSignInSerializer
from users.models               import User
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(['POST'])
def id_check(request):
    if request.method == 'POST':
        serializer = UserIDSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors, status=400)
    return JsonResponse(serializer.data, status=201)
    
class SignUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer
        

                  
class SignInView(APIView):
    serializer_class = UserSignInSerializer  
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
      
        access  = serializer.validated_data['access']
        refresh = serializer.validated_data['refresh']
        
        return JsonResponse({
                'access' : access,
                'refresh': refresh
         },status=200)


class InfoView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        user       = request.user
        user_point = user.point
        user_card  = user.card_number
        return JsonResponse({
            "point"       : user_point,
            "card_number" : user_card
                             },status=200)
      
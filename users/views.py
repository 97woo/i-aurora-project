from django.http                  import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views      import APIView
from rest_framework.decorators import api_view
from .serializers              import UserSignUpSerializer, UserIDSerializer
from users.models              import User
from rest_framework.response import Response


@api_view(['POST'])
def id_check(request):
    if request.method == 'POST':
        serializer = UserIDSerializer(data=request.data)
        
        if serializer.is_valid():
            return JsonResponse(serializer.data,status=200)
        else:
            return Response(serializer.errors, status=404)
    return JsonResponse(serializer.data, status=201)
    
class SignUpView(APIView):
    def post(self,request):
            
            serializer = UserSignUpSerializer(data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
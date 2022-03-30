from django.http                  import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers           import UserSerializer
from rest_framework.views   import APIView


class SignUp(APIView):
    def post(self,request):
            serializer = UserSerializer(data=request.data)
         
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
    

class SignIn(APIView):
    def get(self, request):
            serializer = UserSerializer(data=request.data)
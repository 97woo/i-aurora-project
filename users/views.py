from django.http                  import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views         import APIView

from .serializers           import UserSerializer
from users.models           import User
from rest_framework.parsers import JSONParser

class SignUpView(APIView):
    def post(self,request):
            serializer = UserSerializer(data=request.data)
            print(request)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


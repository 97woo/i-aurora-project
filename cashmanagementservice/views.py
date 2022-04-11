from rest_framework.permissions import IsAuthenticated
from rest_framework.views       import APIView
from .serializers               import SendMoneySerializer
from rest_framework.response    import Response

class SendMoneyView(APIView):
    permission_classes = (IsAuthenticated,)
     
    def post(self,request):
        serializer = SendMoneySerializer(request.data)
        
        return Response(serializer.data,status=204)
        
 
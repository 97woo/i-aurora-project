from rest_framework.views       import APIView

from .serializer                import AccountCheckSerializer
from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated

class AccountCheckView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountCheckSerializer
    
    def post(self, request):
        serializer     = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializers  =  serializer.validated_data
            return Response(serializers,status=200)
        else:
            return Response(serializer.errors, status=400)

        
from django.http                import JsonResponse
from rest_framework.views       import APIView
from .models                    import Bank, AccountHolder
from .serializer                import AccountCheckSerializer
from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework             import serializers

class AccountCheckView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        lookup_field = 'name'
        serializer = AccountCheckSerializer(
           data=
                {
                "bank"           : request.data['bank'],
                "account_number" : request.data['account_number'],
                "name"           : lookup_field
                })
        print(serializer)
        if serializer.is_valid(raise_exception=True):
    
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors, status=400)
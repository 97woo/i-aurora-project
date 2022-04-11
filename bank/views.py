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
        queryset_account    = AccountHolder.objects.get(account_number=request.data['account_number'])
        serializer  = AccountCheckSerializer(
           data=
                {
                "bank"           : request.data['bank'],
                "account_number" : request.data['account_number'],
                "name"           : queryset_account.name
                })
        
        if serializer.is_valid(raise_exception=True):
            print(serializer)  
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors, status=400)
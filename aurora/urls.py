
from django.contrib import admin
from django.urls import path, include
   

urlpatterns = [
    path('users', include('users.urls')),
    path('banks', include('bank.urls')),
    path('cms'  , include('cashmanagementservice.urls'))
]
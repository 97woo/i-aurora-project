from django.urls               import path
from cashmanagementservice     import views

urlpatterns = [
    path('/send',views.SendMoneyView.as_view()),
]    
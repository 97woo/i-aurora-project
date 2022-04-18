from django.urls               import path
from cashmanagementservice     import views

urlpatterns = [
    path('/send',views.SendMoneyView.as_view()),
    path('/memo',views.SendMemoView.as_view()),
    path("/memo/<int:pk>", views.SendMemoView.as_view()),
]   
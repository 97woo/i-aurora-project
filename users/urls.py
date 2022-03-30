from django.urls import path, include
from users       import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view()),
]    
from django.urls import path, include
from users       import views
from .views       import id_check

urlpatterns = [
    path('signup/', views.SignUpView.as_view()),
    path('idcheck/', id_check),
]    
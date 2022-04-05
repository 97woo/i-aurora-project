from django.urls  import path
from users        import views
from .views       import id_check

urlpatterns = [
    path('/signup', views.SignUpView.as_view()),
    path('/idcheck', id_check),
    path('/signin', views.SignInView.as_view()),
    path('/point', views.PointView.as_view())
]    
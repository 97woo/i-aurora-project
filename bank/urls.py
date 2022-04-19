from django.urls  import path
from bank        import views

urlpatterns = [
    path('/account', views.AccountCheckView.as_view()),
]    
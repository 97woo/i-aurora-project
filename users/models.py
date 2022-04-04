from django.db   import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, identification, password,point):        
        
        user = self.model(            
            identification = identification,
        ) 
        user.set_password(password)
        return user     



class User(AbstractBaseUser):
    objects = UserManager()
    
    identification     = models.CharField(max_length=100, unique=True)
<<<<<<< HEAD
    point              = models.DecimalField(decimal_places=2, max_digits = 20, default=1000)
=======
    point              = models.DecimalField(decimal_places=2, max_digits = 20, default=1000000)
>>>>>>> feature/simplejwt
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD  = 'identification'
    
    class Meta:
          db_table = 'users'
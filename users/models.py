from django.db   import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import random

class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, identification, password, point, card_number):        
        
        user = self.model(            
            identification = identification,
            card_number    = random.randint(999,10000)
        ) 
        user.set_password(password)
        return user     



class User(AbstractBaseUser):
    objects = UserManager()
    
    identification     = models.CharField(max_length=100, unique=True)
    point              = models.PositiveIntegerField(default=1000000)
    card_number        = models.CharField(max_length=50, unique=True, null=True)
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD  = 'identification'
    
    class Meta:
          db_table = 'users'
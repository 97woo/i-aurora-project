from turtle import update
from django.db   import models

class User(models.Model):
    trinity_id         = models.CharField(max_length=100, unique=True)
    trinity_password   = models.PositiveIntegerField()
    point              = models.DecimalField(decimal_places=2, max_digits = 20, default=1000)
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now=True)
    
    class Meta:
          db_table = 'users'
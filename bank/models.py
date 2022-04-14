from django.db import models

class Bank(models.Model):
    name     = models.CharField(max_length=50)
    bankcode = models.IntegerField()
    
    class Meta:
        db_table = 'banks'
        
class AccountHolder(models.Model):
    name           = models.CharField(max_length=100)
    account_number = models.CharField(max_length=250)
    deposit        = models.PositiveIntegerField()
    bank           = models.ForeignKey("Bank", related_name='banks', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'account_holders'
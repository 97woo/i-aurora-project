from django.db import models

class Send(models.Model):
    amount      = models.BigIntegerField()
    bankcode    = models.IntegerField()
    fee         = models.IntegerField()
    remittor    = models.CharField(max_length=30)
    recipient   = models.CharField(max_length=30)
    account_no  = models.CharField(max_length=50)
    bank_name   = models.CharField(max_length=10)
    user        = models.ForeignKey('users.User', on_delete=models.CASCADE)
    create_at   = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'sends'
        

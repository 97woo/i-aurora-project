from django.db import models

class Send(models.Model):
    amount      = models.BigIntegerField()
    bankcode    = models.IntegerField()
    fee         = models.IntegerField(default=500)
    remittor    = models.CharField(max_length=20)
    recipient   = models.CharField(max_length=20)
    account_no  = models.CharField(max_length=40)
    bank_name   = models.CharField(max_length=20)
    user        = models.ForeignKey('users.User', related_name='senduser', on_delete=models.CASCADE)
    create_at   = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'sends'
        

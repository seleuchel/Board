from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    vul_ok = models.BooleanField(default=False)
    srv_name = models.CharField(max_length=100)
    req_date = models.DateField()
    sendmail_date = models.DateField()
    adm_buseo = models.CharField(max_length=30)
    adm_name = models.CharField(max_length=15)
    srv_loc = models.CharField(max_length=50)
    bigo = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.srv_name
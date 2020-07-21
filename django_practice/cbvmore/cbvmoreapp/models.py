from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,default =1,on_delete = models.CASCADE) #로그인한 유저 settings.AUTH_USER_MODE
    time = models.DateTimeField(default=timezone.now) #생성시간 자동으로 들어가게 

from django.db import models

# Create your models here.
class FirstModel(models.Model):
    x = (
        ('Good','좋아요'),
        ('Bad','싫어요'),
    )
    text = models.TextField()
    title = models.CharField(max_length=50)
    recommend = models.CharField(max_length=5 , choices=x) #defalut 값으로 들어간다 good,bad=> max_length에 해당

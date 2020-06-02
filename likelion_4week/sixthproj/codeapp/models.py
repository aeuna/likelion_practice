from django.db import models

# Create your models here.
class imgintroduction(models.Model):
    img_name = models.CharField(max_length=50)
    img_description = models.TextField()
    img = models.ImageField(upload_to= "image" , blank = True)

def __str__(self):
    return self.img_name

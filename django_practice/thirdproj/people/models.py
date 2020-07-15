from django.db import models

# Create your models here.

class person(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField(auto_now=False)
    age = models.IntegerField()
    department = models.CharField(max_length=20)
    fav = models.TextField(blank=True)

    def __str__(self):
        return self.name #나이로 하고싶으면 self.age
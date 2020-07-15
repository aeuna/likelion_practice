from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length= 200)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE) #참조하는 테이블의 행이 삭제되면 대응되는 행들도 같이 삭제 혹은 갱신
    choice_text = models.CharField(max_length= 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text

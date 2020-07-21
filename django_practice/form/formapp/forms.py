from django import forms
from .models import FirstModel

class Fisrtform(forms.Form):
    recommend = (
        ('Good','좋아요'), #저장되는건 good 표시되는건 좋아요로 표시
        ('Bad','싫어요'),
    )
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea) #forms에는 textarea없음.
    choice = forms.ChoiceField(choices=recommend)

class Secondform(forms.ModelForm):
    class Meta:
        model = FirstModel
        fields = ['title','text','recommend']
from django.shortcuts import render
import datetime #날짜띄우기

# Create your views here.
# 정보를 넣어주는 곳이라 생각
def home(request): #렌더 시켜주는 함수
    a=3
    b=6
    c=a+b
    name="euna"
    now = datetime.datetime.now() #정적으로 그냥 띄울때 시간을 보여줌
    day = ['mon','tue','wed']
    return render(request,'firstapp_templates/home.html',{"int" : c,"user":name, "now":now, "day":day})

def first(request):
    return render(request,'firstapp_templates/first.html')

def second(request):
    return render(request,'firstapp_templates/second.html')

def third(request):
    return render(request,'firstapp_templates/third.html')
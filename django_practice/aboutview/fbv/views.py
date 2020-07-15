# from django.shortcuts import render,get_object_or_404
# from .models import Question,Choice
# from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse

# Create your views here.
def index(request):
    # question = Question.objects.all()
    # return render(request, 'index.html')
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #()안 모델 필드 기준
    return render(request,'fbv/index.html',{'latest_question_list':latest_question_list})


def detail(request,question_id):
    # detail = get_object_or_404(Question,pk=question_id)
    # return render(request,'detail.html',{'content':detail})
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question' : question
    }
    return render(request,'fbv/detail.html',context)

def results(request,question_id):
    question =get_object_or_404(Question,pk=question_id)
    return render(request,'fbv/results.html',{'question':question})


def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #choice_set  https://cosmian.tistory.com/124 참고
    except (KeyError,Choice.DoesNotExit):
        return render(request, 'fbv/detail.html', {'question':question, 'error_msg':"you didn't select a choice"})
        #투표할수 있는 페이지로 다시 넘어간다
    else:
        selected_choice.votes += 1
        selected_choice.save() #갱신된걸 다시 저장
    return HttpResponseRedirect(reverse('fbv:results', args=(question.id,)))

#render 템플릿으로 연결을 한다. 데이터를 뿌린데 redirect 인자는 url 템플릿연결이 아니라 url연결  한번더 view로 지나간다. MTV패턴??
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

# Create your views here.

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExit):
        return render(request, 'cbv/detail.html', {'question':question, 'error_msg':"you didn't select a choice"})
        #투표할수 있는 페이지로 다시 넘어간다
    else:
        selected_choice.votes += 1
        selected_choice.save() #갱신된걸 다시 저장
    return HttpResponseRedirect(reverse('cbv:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'cbv/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self): #django 개발 문서를 보시오. listview 쪽을 봐라 list를 가지고 오는 함수.
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView): #pk를 지가 알아서 받아옴
    model = Question
    template_name = 'cbv/detail.html' #템플릿 경로를 적기만 하면 됨

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'cbv/results.html'
from django.urls import path

from . import views

app_name = 'cbv' #namespace app이 여러개일때, 어느 앱의 url name인지 헷갈리니까 namespace를 이용해서 fbv의 detail이야 라고 알려주는것
urlpatterns=[
    path('',views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(), name='detail'), #한가지 html에 여러개 view 가 올수 있음
    path('<int:pk>/results/',views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/',views.vote, name='vote'), #한가지 html에 여러개 view 가 올수 있음
]
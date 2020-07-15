from django.urls import path

from . import views

app_name = 'fbv' #namespace app이 여러개일때, 어느 앱의 url name인지 헷갈리니까 namespace를 이용해서 fbv의 detail이야 라고 알려주는것
urlpatterns=[
    path('',views.index, name='index'),
    path('<int:question_id>/',views.detail, name='detail'), #한가지 html에 여러개 view 가 올수 있음
    path('<int:question_id>/results/',views.results, name='results'),
    # path('<int:question_id>/vote/',views.vote, name='vote'), #한가지 html에 여러개 view 가 올수 있음
]
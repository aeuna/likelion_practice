from django.shortcuts import render,get_object_or_404,redirect
from .models import Youtube

# Create your views here.
def introduction(request):
    youtube = Youtube.objects
    return render(request , 'introduction.html' , {'youtube' : youtube})

def detail(request,detail_id):
    detail = get_object_or_404(Youtube , pk=detail_id)
    return render(request,'detail.html',{'content':detail})

def create(request):
    youtube = Youtube()
    youtube.channel_name = request.POST['name']
    youtube.creator_name = request.POST['creator']
    youtube.followers = request.POST['subscribe_num']
    youtube.popularity = request.POST['popular']
    youtube.link1 = request.POST['youtube_link_1']
    youtube.link2 = request.POST['youtube_link_2']
    youtube.link3 = request.POST['youtube_link_3']
    youtube.summary = request.POST['summary']
    youtube.text = request.POST['text']
    youtube.onair = request.POST['choices']
    youtube.save()
    return redirect('introduction')

def new(request):
    return render(request , 'new.html')


    
    

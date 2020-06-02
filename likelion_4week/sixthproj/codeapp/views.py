from django.shortcuts import render,get_object_or_404
from .models import imgintroduction
from .forms import createForm

# Create your views here.
def home(request):
    imginfo = imgintroduction.objects
    return render(request,'home.html',{"imginfo":imginfo})

def detail(request,detail_id):
    detail = get_object_or_404(imgintroduction,pk=detail_id)
    return render(request,'detail.html',{'content':detail})

def new(request):
    form = createForm()
    if request.method =='POST':
        pass
    elif request.method == 'GET':
        form = createForm()
        return render(request,'new.html',{'form':form})
    else:
        pass

def create(request):
    imginfo = imgintroduction()
    imginfo.img_name = request.POST['name']
    imginfo.img_description = request.POST['description']
    imginfo.img = request.FILES['photo']
    imginfo.save()
    return redirect('home')
from django.shortcuts import render
from .forms import Fisrtform,Secondform
# Create your views here.
def index(request):
    form = Fisrtform()
    form2 = Secondform
    return render(request, 'index.html', {'form':form, 'form2':form2})

from django.shortcuts import render
from django.views.generic.list import ListView #전부 가져온다.
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from . models import Blog

# Create your views here.
def result(request):
    BlogPosts = Blog.objects.all()
    query = request.GET.get('query','') #name: query에 해당하는 걸 가져온다 
    if query:
        BlogPosts = BlogPosts.filter(Q(title__icontains=query)| Q(text__icontains=query)).order_by('-time')
    return render(request, 'result.html',{'BlogPosts':BlogPosts , 'query':query})

class index(ListView):
    template_name = 'index.html'
    context_object_name = 'blog_list' #데이터 리스트를 다 가져오겠다. blog_list를 통해서... 
    def get_queryset(self):
        return Blog.objects.all

class detail(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'blog'

class delete(DeleteView):
    model = Blog
    template_name = 'delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('index')

class update(UpdateView):
    model = Blog
    template_name = 'update.html'
    fields = ['title','text']
    success_url = reverse_lazy('index')

class create(CreateView):
    model = Blog
    template_name = 'create.html'
    fields = ['title','text']
    def form_valid(self,form): #form 유효성 검사 => author가 글을 작성한 author인지...
        Blog = form.save(commit=False)
        Blog.author = self.request.user
        Blog.save()

        return HttpResponseRedirect(self.request.POST.get('next','/'))
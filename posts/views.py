from django.shortcuts import render
from .models import Post
# Create your views here.


def all_posts(request):
    posts = Post.objects.all()         #''' select * from posts '''
    return render(request,'posts.html',{'mahmoud':posts})


def single_post(request,id):
    post = Post.objects.get(id=id)
    return render(request,'single.html', {'single_post':post})
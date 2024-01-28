from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Dave Smith',
        'title': 'Blog post 1',
        'content': 'Demo post',
        'date_posted': 'January 27, 2024'
    },
    {
        'author': 'Gregor Mendel',
        'title': 'Blog post 2',
        'content': 'Demo post 2',
        'date_posted': 'January 30, 2024'
    }
]

def home(request):
    context = {
        'post': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


    

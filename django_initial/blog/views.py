from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'test1',
        'title' : 'Django post 1',
        'content' : 'First Django PJT',
        'date_posted' : 'May 1, 2020',
    },
    {
        'author': 'test2',
        'title': 'Django post 2',
        'content': 'First Django PJT',
        'date_posted': 'May 2, 2020',
    }
]


# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)


def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title':'About'})
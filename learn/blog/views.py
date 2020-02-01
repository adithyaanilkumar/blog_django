from django.shortcuts import render
from django.http import HttpResponse
posts=[
    {
        'author':'Adithya',
        'Title': 'blog post 1',
        'content':'first post',
        'date_posted':'August 27,2018',
    },
    {
        'author':'amma',
        'Title': 'blog post 2',
        'content':'second post',
        'date_posted':'August 28,2018',
    }
]

# Create your views here.
def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
from django.shortcuts import render
from blog.data import posts

# Create your views here.
def blog(request):

    context = {
        'text': 'Olá Blog',
        'posts': posts
    }
    return render(request, "blog/index.html", context)
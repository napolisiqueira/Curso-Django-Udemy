from django.shortcuts import render

# Create your views here.
def home(request):

    contexto = {
        'text': 'Estamos na Home!!'
    }
    return render(request, "home\index.html", contexto)
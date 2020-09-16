from django.shortcuts import render

# Create your views here.

def index(request):
    """ Index page view """

    return render(request, 'home/index.html')

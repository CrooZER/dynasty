from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def managers(request):
    return render(request, 'managers.html')
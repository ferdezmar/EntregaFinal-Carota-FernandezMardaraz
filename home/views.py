from django.shortcuts import render


def about(request):
    return render(request, 'home/about.html')


def index(request):
    return render(request, 'home/index.html')
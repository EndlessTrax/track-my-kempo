from django.shortcuts import render


def home(request):
    return render(request, 'kempo/index.html')


def training_log(request):
    return render(request, 'kempo/training.html')

from django.shortcuts import render, redirect
from django.contrib import messages
# from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, AddTechnique
from .models import Technique

from datetime import datetime

# from django.views.generic import ListView

# class SomeListView(ListView):
#     model = Technique
#     template_name = 'kempo/home.html'
#     context_object_name = ''


def home(request):
    return render(request, 'kempo/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created {username}! You are now able to log in.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'kempo/register.html', {'form': form})


@login_required
def training_log(request):
    user_techniques = Technique.objects.filter(author=request.user)
    list_of_techniques = user_techniques.order_by('title')
    return render(request, 'kempo/training.html', {'list_of_techniques': list_of_techniques})


@login_required
def technique_update(request, id):
    to_update = Technique.objects.get(pk=id)
    to_update.date_practiced = datetime.now()
    to_update.save()
    messages.info(request, f'{to_update.title} updated!')
    return redirect('training-log')


@login_required
def add_new_technique(request):
    if request.method == 'POST':
        form = AddTechnique(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('technique')
            author = User.objects.get(username=request.user)
            new_technique = Technique(title=title, author=author)
            new_technique.save()
            messages.success(request, f'You have added {title} to your Log.')
            return redirect('training-log')
    else:
        form = AddTechnique()
    return render(request, 'kempo/new-technique.html', {'form': form})

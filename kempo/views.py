from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, AddTechnique
from .models import Technique

# from django.views.generic import ListView

# class SomeListView(ListView):
#     model = Technique
#     template_name = 'kempo/home.html'
#     context_object_name = ''


def home(request):
    if request.user.is_authenticated:
        user_techniques = Technique.objects.filter(author=request.user).order_by('date_practiced')
        # list_of_techniques = user_techniques.order_by('date_practiced')
        list_of_techniques = user_techniques.filter()[:5]
        return render(request, 'kempo/index.html', {'list_of_techniques': list_of_techniques})
    else:
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
    list_of_categories = []
    for item in user_techniques:
        if item.category not in list_of_categories:
            list_of_categories.append(item.category)
       
    return render(request, 'kempo/training.html', 
                    {'list_of_techniques': list_of_techniques, 'list_of_categories': list_of_categories})


@login_required
def technique_update(request, id):
    to_update = Technique.objects.get(pk=id)
    to_update.date_practiced = timezone.now()
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
            category = form.cleaned_data.get('category')
            notes = form.cleaned_data.get('notes')
            new_technique = Technique(title=title, category=category, author=author, notes=notes)
            new_technique.save()
            messages.success(request, f'You have added {title} to your Log.')
            return redirect('training-log')
    else:
        form = AddTechnique()
        return render(request, 'kempo/new-technique.html', {'form': form})


@login_required
def single_technique(request, id):
    current_technique = Technique.objects.get(pk=id)
    return render(request, 'kempo/single-technique.html', {'technique': current_technique})


@login_required
def edit_technique(request, id):
    current_technique = Technique.objects.get(pk=id)
    if request.method == 'POST':
        form = AddTechnique(request.POST)
        if form.is_valid():
            updated_title = form.cleaned_data.get('technique')
            # updated_author = User.objects.get(username=request.user)
            updated_notes = form.cleaned_data.get('notes')
            updated_category = form.cleaned_data.get('category')
            current_technique.title = updated_title
            current_technique.category = updated_category
            current_technique.notes = updated_notes
            current_technique.save()
            messages.success(request, f'Update Successful!')
            return redirect('single-technique', id)
    else:
        form = AddTechnique(initial={'technique': current_technique.title, 'notes': current_technique.notes})        
    return render(request, 'kempo/edit-technique.html', {'technique': current_technique, 'form': form})


@login_required
def delete_technique(request, id):
    current_technique = Technique.objects.get(pk=id)
    current_technique.delete()
    return redirect('training-log')
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import train
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

""" def railhome(request): 
    context ={
        'posts': train.objects.all()
    }
    return render(request, 'railway/rail_home.html', context) """

def index(request):
    lis = train.objects.all()
    return render(request, 'railway/alltrains.html', {"lis": lis})

def findtrains(request):
    
    trains = train.objects.values('source', 'destination').distinct()
    
    source = trains.values_list('source', flat=True).distinct()
    destination = trains.values_list('destination', flat=True).distinct()

    return render(request, 'railway/findtrains.html', {'source': source, 'destination': destination})

def train_filter(request):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        filtered_trains = train.objects.filter(source=source, destination=destination)

        return render(request, 'railway/result.html', {'filtered_trains': filtered_trains})

    return render(request, 'railway/rail_base.html')  

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def register(request): 
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #if submitted
            form.save() #saves the information filled in (new user is created)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been creted. u can login!')
            return redirect('login')
            
    else:
        form = UserRegisterForm() 
    
    return render(request, 'users/register.html', {'form': form})
def logoutuser(request):
    logout(request)
    return redirect('/')



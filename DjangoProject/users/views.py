from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


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
    #i want to redirect to my logout.html page
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been updated. u can login!')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm( instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html',context)




from django.shortcuts import render,redirect, HttpResponse
from .forms import CustomUserCreationForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return render(request,'users/login.html')
@login_required
def profile(request):
    return render(request,'users/profile.html')

@login_required
def edit_profile(request):
    if request.method=='POST':
        user = request.user
        u_form = UserUpdateForm(request.POST,instance=user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        user = request.user
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)
    return render(request,'users/edit-profile.html',{'u_form':u_form,'p_form':p_form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('login')
    return render(request,'users/delete-profile.html')

@login_required
def change_password(request):
    if request.method == "POST":
        pswd = PasswordChangeForm(user=request.user,data=request.POST)
        if pswd.is_valid():
            user=pswd.save()
            update_session_auth_hash(request,user)
            return redirect('index')
    else:
        pswd = PasswordChangeForm(request.user)
    return render(request,'users/change-password.html',{'pswd':pswd})
            


    

    




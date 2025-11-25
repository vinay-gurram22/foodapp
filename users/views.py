from django.shortcuts import render,redirect, HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
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
    return render(request,'users/logout.html')

def profile(request):
    return render(request,'users/profile.html')


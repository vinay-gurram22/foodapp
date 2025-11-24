from django.shortcuts import render,redirect, HttpResponse
from .forms import CustomUserCreationForm
# Create your views here.
def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse(f"user is succesfully registed")
    return render(request, 'users/register.html', {'form': form})





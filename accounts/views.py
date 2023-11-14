from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form, 
    }
    return render(request, 'accounts_form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('posts:index')
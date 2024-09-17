from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect(reverse('learning_logs:index'))



def register(request):
    '''register new user.'''
    if request.method != 'POST':
        # show blank register form.
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # automatic log in,and redirect.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect(reverse('learning_logs:index'))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)
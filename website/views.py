from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm


def main(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('tasks')
        else:
            messages.success(request, 'Try again')
            return redirect('tasks')

    else:
        return render(request, 'tasks.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('tasks')


def register_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,
                             "You Have Successfully Registered! Welcome!")
            return redirect('tasks')
    else:
        form = NewUserForm()
        return render(request, 'register.html', {'register_form': form})

    return render(request, 'register.html', {'register_form': form})

from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm


def services(request):
    service = Service.objects.all()
    return render(request, 'services.html', {'services': service})


def create_service(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('services')
    return render(request, 'create_service.html', {'form': form})

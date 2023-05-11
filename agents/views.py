from django.shortcuts import render, redirect
from .models import Profile, Org
from .forms import ProfileForm, UserForm, AddressForm, OrgForm
from .filters import ProfileFilter
from django.contrib import messages


def show_agents(request):
    agents = Profile.objects.all()
    filter_agents = ProfileFilter(request.GET, queryset=agents)
    agents = filter_agents.qs
    return render(
        request, 'agents.html', {'agents': agents, 'filter': filter_agents})


def show_detail_agents(request, pk):
    current = Profile.objects.get(id=pk)
    return render(
        request, 'current_agent.html', {'current': current})


def create_agent(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('agents')
    return render(request, 'create_agent.html', {'form': form})


def create_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('agents')
    return render(request, 'create_agent.html', {'form': form})


def create_org(request):
    form = OrgForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('agents')
    return render(request, 'create_agent.html', {'form': form})


def create_address(request):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('agents')
    return render(request, 'create_agent.html', {'form': form})


def update_address(request, pk):
    current = Profile.objects.get(id=pk)
    form = AddressForm(request.POST or None, instance=current.address)
    if form.is_valid():
        form.save()
        return redirect('current_agent', pk)
    return render(request, 'update_agent.html', {'form': form, 'pk': pk})


def update_agent(request, pk):
    current = Profile.objects.get(id=pk)
    form = ProfileForm(request.POST or None, instance=current)
    if form.is_valid():
        form.save()
        return redirect('current_agent', pk)
    return render(request, 'update_agent.html', {'form': form, 'pk': pk})


def update_user(request, pk):
    current = Profile.objects.get(id=pk)
    form = UserForm(request.POST or None, instance=current.user)
    if form.is_valid():
        form.save()
        return redirect('current_agent', pk)
    return render(request, 'update_agent.html', {'form': form, 'pk': pk})


def update_org(request, pk):
    current = Profile.objects.get(id=pk)
    form = OrgForm(request.POST or None, instance=current.org)
    if form.is_valid():
        form.save()
        return redirect('current_agent', pk)
    return render(request, 'update_agent.html', {'form': form, 'pk': pk})


def delete_profile(request, pk):
    current = Profile.objects.get(id=pk)
    try:
        current.delete()
    except Exception:
        messages.success(request, 'Невозможно удалить контрагента, так как существует обращение.')
        return redirect('current_agent', pk)
    return redirect('agents')

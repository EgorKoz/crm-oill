from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appeal
from .forms import AppealForm


def appeal(request):
    appeals = Appeal.objects.all()
    return render(
        request, 'appeal.html', {'appeals': appeals})


def appeal_current(request, pk):
    agent_id = request.GET.get('id', '')
    current = Appeal.objects.get(id=pk)
    return render(
        request, 'current_appeal.html', {'current': current,
                                         'agent_id': agent_id})


def appeal_create(request):
    form = AppealForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        return redirect('appeal')
    return render(request, 'create_appeal.html', {'form': form})


def appeal_update(request, pk):
    current = Appeal.objects.get(id=pk)
    form = AppealForm(request.POST or None, instance=current)
    if form.is_valid():
        form.save()
        return redirect('appeal_current', pk)
    return render(request, 'update_appeal.html', {'form': form, 'pk': pk})


def delete_appeal(request, pk):
    current = Appeal.objects.get(id=pk)
    try:
        current.delete()
    except Exception:
        messages.success(request, 'Невозможно удалить обращение, так как существует заявка.')
        return redirect('appeal_current', pk)
    return redirect('appeal')

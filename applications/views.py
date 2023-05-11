from django.shortcuts import render, redirect
from .models import Application
from appeal.models import Appeal
from .forms import ApplicationForm
from services.forms import ServiceForm
from contracts.forms import ContractForm


def app(request):
    apps = Application.objects.all()
    return render(
        request, 'applications.html', {'apps': apps})


def app_current(request, pk):
    agent_id = request.GET.get('id', '')
    current = Application.objects.get(id=pk)
    return render(
        request, 'current_application.html', {'current': current,
                                              'agent_id': agent_id})


def create_app_form(request):
    pk = request.GET.get('id', '')
    if pk:
        current = Appeal.objects.get(id=pk)
    if request.method == 'POST':
        form_app = ApplicationForm(request.POST)
        form_srv = ServiceForm(request.POST)
        form_ctr = ContractForm(request.POST, request.FILES,
                                instance=current.contract)
        if form_srv.is_valid():
            form_srv.save()
            form_srv = ServiceForm()
            form_app = ApplicationForm(instance=current)
            form_ctr = ContractForm(instance=current.contract)
        if form_ctr.is_valid() and form_app.is_valid():
            ctr = form_ctr.save(commit=False)
            srv = form_ctr.cleaned_data.get('services')
            ctr.profile = current.client
            ctr.created_by = request.user
            ctr.save()
            ctr.services.set(srv)
            ctr.save()
            current.contract = ctr
            current.status = 'r'
            current.save()
            appl = form_app.save(commit=False)
            appl.appeal = current
            appl.save()
            return redirect('applications')
    else:
        form_app = ApplicationForm(instance=current, )
        form_srv = ServiceForm()
        form_ctr = ContractForm(instance=current.contract)

    return render(request, 'create_application.html',
                  {'form_app': form_app,
                   'form_srv': form_srv,
                   'form_ctr': form_ctr,
                   'current': current})


def update_app(request, pk):
    current = Application.objects.get(id=pk)
    if request.method == 'POST':
        form_app = ApplicationForm(request.POST, instance=current)
        form_srv = ServiceForm(request.POST)
        form_ctr = ContractForm(request.POST, request.FILES,
                                instance=current.appeal.contract)
        if form_srv.is_valid():
            form_srv.save()
            form_srv = ServiceForm()
            form_app = ApplicationForm(instance=current)
            form_ctr = ContractForm(instance=current.appeal.contract)
        if form_ctr.is_valid() and form_app.is_valid():
            ctr = form_ctr.save(commit=False)
            srv = form_ctr.cleaned_data.get('services')
            ctr.profile = current.appeal.client
            ctr.created_by = request.user
            ctr.save()
            ctr.services.set(srv)
            ctr.save()
            current.appeal.contract = ctr
            current.appeal.save()
            appl = form_app.save(commit=False)
            appl.appeal = current.appeal
            appl.save()
            return redirect('app_current', pk)
    else:
        form_app = ApplicationForm(instance=current)
        form_srv = ServiceForm()
        form_ctr = ContractForm(instance=current.appeal.contract)

    return render(request, 'update_application.html',
                  {'form_app': form_app,
                   'form_srv': form_srv,
                   'form_ctr': form_ctr,
                   'current': current})


def send_app(request, pk):
    pass

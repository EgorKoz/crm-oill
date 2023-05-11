from django.shortcuts import render
from .forms import ContractForm


def contracts(request):
    form_ctr = ContractForm(request.POST or None)
    if form_ctr.is_valid():
        form_ctr.save()
    return render(request, 'contracts.html', {'form_ctr': form_ctr})

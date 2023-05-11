from django.shortcuts import render, redirect
from applications.models import Application
from .models import Offer


def offers(request):
    offer = Offer.objects.all()
    return render(request, 'offers.html', {'offers': offer})


def offer_current(request, pk):
    agent_id = request.GET.get('id', '')
    current = Offer.objects.get(id=pk)
    return render(request, 'current_offer.html', {'current': current,
                                                  'agent_id': agent_id})


def create_offer(request):
    app_id = request.GET.get('id', '')
    app = Application.objects.get(id=app_id)
    contract = app.appeal.contract
    offer = Offer(
        contract=contract,
        created_by=request.user,
    )
    offer.save()
    app.status = 'c'
    app.save()
    return redirect('offer_current', offer.id)

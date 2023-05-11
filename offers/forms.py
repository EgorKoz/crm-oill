from .models import Offer
from django import forms


class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        exclude = ['contract', 'created_by', 'created_on', 'send_on', 'status']
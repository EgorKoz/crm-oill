from .models import Contract
from services.models import Service
from django import forms


class ContractForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Услуги',
    )

    class Meta:
        model = Contract
        exclude = ['profile', 'created_by', 'created_on', 'send_on']

    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'

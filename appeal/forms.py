from .models import Appeal
from agents.models import Profile
from contracts.models import Contract
from django import forms


class AppealForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=Profile.objects.all(),
        label='Контрагент',
        empty_label='',
    )
    contract = forms.ModelChoiceField(
        queryset=Contract.objects.all(),
        label='Договор',
        empty_label='',
        required=False,
    )

    class Meta:
        model = Appeal
        exclude = ['created_by', 'status']

    def __init__(self, *args, **kwargs):
        super(AppealForm, self).__init__(*args, **kwargs)

        self.fields['client'].widget.attrs['class'] = 'form-select'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['topic'].widget.attrs['class'] = 'form-select'
        self.fields['channel'].widget.attrs['class'] = 'form-select'
        self.fields['contract'].widget.attrs['class'] = 'form-select'
        self.fields['closed_on'].widget.attrs['class'] = 'form-control'
        self.fields['comment'].widget.attrs['class'] = 'form-control'

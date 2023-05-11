from .models import Application
from django import forms


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        exclude = ['appeal', 'send_on']

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        self.fields['priority'].widget.attrs['class'] = 'form-select'
        self.fields['status'].widget.attrs['class'] = 'form-select'

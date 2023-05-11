from .models import Profile, Address, Org, User
from django import forms


class ProfileForm(forms.ModelForm):
    org = forms.ModelChoiceField(label="Организация",
                                 queryset=Org.objects.all())
    address = forms.ModelChoiceField(label="Адрес",
                                     queryset=Address.objects.all())
    user = forms.ModelChoiceField(label="Представитель организации",
                                  queryset=User.objects.all())

    class Meta:
        model = Profile
        fields = '__all__'


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'


class OrgForm(forms.ModelForm):

    class Meta:
        model = Org
        fields = '__all__'


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

import django_filters
from .models import *


class CharFilterInFilter(django_filters.BaseInFilter,
                         django_filters.CharFilter):
    pass


class ProfileFilter(django_filters.FilterSet):
    org = CharFilterInFilter(label='Организация', field_name='org__name', lookup_expr='icontains')
    user = CharFilterInFilter(field_name='user__first_name', lookup_expr='in')

    class Meta:
        model = Profile
        fields = '__all__'

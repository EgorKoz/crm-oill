from django.contrib import admin
from .models import Address, Org, Profile, User

admin.site.register(Address)
admin.site.register(Org)
admin.site.register(Profile)
admin.site.register(User)

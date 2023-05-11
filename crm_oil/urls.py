from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('agents/', include('agents.urls')),
    path('services/', include('services.urls')),
    path('apps/', include('applications.urls')),
    path('appeals/', include('appeal.urls')),
    path('contracts/', include('contracts.urls')),
    path('offers/', include('offers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

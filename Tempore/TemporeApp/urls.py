from django.conf.urls import url, include
from django.urls import path
from TemporeApp import views
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^person$', views.get_person_coordinates_from_location),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home')
]

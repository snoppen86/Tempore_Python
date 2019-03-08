from django.conf.urls import url, include
from django.urls import path
from TemporeApp import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('status/', views.travel_status),
    path('person/', views.get_person_coordinates_from_location),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # path('status/', views.get_travel_status()),
]

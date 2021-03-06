import logging
import json
from django.http import QueryDict
from django.shortcuts import render,redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.travelStatus import get_travel_status
from .services.response_service import main_response_handler
from .core.forms import SignUpForm, EditProfileForm

log = logging.getLogger(__file__)


@api_view(['POST'])
def get_person_coordinates_from_location(request):
    try:
        data = request.POST
        log.info(f"{data['Name']}, {data['address']}")
        response_service = main_response_handler(data)
        return Response(response_service)
    except:  # NOQA
        log.warning("Failed to get location", exc_info=True)
    return Response(status=404)

def render_website(request):
    return render(request, '/index.html')

@api_view(['GET'])
def travel_status(request):
    travel_status_response = get_travel_status()
    return Response(travel_status_response)


def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('passqord1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('login')
            except:
                log.exception("Failed to save sign up")
        else:
            log.error("Form is not valid")
    form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html', args)


def edit_profile(request):
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('view_profile')
        else:
            form = EditProfileForm(instance=request.user)
            args = {'form': form }
            return render(request, 'registration/edit_profile.html', args)


def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('view_profile')
            else:
                return redirect('change_password')
        else:
            form = PasswordChangeForm(user=request.user)
            args = {'form': form}
            return render(request, 'registration/change_password.html', args)




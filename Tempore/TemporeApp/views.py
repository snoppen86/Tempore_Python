import logging
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.response_service import main_response_handler
from .core.forms import SignUpForm

log = logging.getLogger(__file__)


@api_view(['POST'])
def get_person_coordinates_from_location(request):
    try:
        data = request.data
        response_service = main_response_handler(data)
        return Response(response_service)
    except:  # NOQA
        log.warning("Failed to get location", exc_info=True)
    return Response(status=404)

def render_website(request):
    return render(request, '/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('passqord1')
            user = authenticate(username=username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index.html')
        else:
            form = SignUpForm
            return render(request, 'signup.html', {'form': form})

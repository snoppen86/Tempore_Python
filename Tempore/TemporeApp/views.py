import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.response_service import main_response_handler

log = logging.getLogger(__file__)


@api_view(['POST', 'GET'])
def get_person_coordinates_from_location(request):
    try:
        data = request.data
        response_service = main_response_handler(data)
        return Response(response_service)
    except:  # NOQA
        log.warning("Failed to get location", exc_info=True)
    return Response(status=404)

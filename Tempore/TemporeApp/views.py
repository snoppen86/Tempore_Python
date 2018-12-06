import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.location import get_coordinates_for_location
from .services.Slrequest import get_trip_from_coordinates
from .services.schdule import schdule_start_end_time_switcher
log = logging.getLogger(__file__)

@api_view(['POST', 'GET'])
def get_person_coordinates_from_location(request):
    try:
        data = request.data
        log.info(f"Got {data}")
        person = data['person']
        location = get_coordinates_for_location(person['address'])
        #schdule_check = schdule_start_end_time_switcher(person['scheduleStart'], person['scheduleEnd'])
        commute_travel_plan = get_trip_from_coordinates(location, person['scheduleStart'])
        return Response({'Travel plan': commute_travel_plan})
    except:  # NOQA
        log.warning("Failed to get location", exc_info=True)
    return Response(status=404)



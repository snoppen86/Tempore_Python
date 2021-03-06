import requests
import logging
log = logging.getLogger(__file__)

URL = "https://geocoder.api.here.com/6.2/geocode.json?app_id=rh8e4vbpg3DqRj61Nes5&app_code=-nm97oRF_yvf90ACG5tJFw\
"


# Here maps på google

def get_coordinates_for_location(location: str):
    reps = location.replace(' ', '+')
    param = "&searchtext=" + reps
    r = requests.get(url=URL, params=param)
    resp_location = _get_location_from_response(r.json())
    display_position = resp_location['DisplayPosition']
    return f"&originCoordLat={display_position['Latitude']}" + f"&originCoordLong={display_position['Longitude']}"


def _get_location_from_response(data):
    return data['Response']['View'][0]['Result'][0]['Location']

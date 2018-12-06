import requests

URL = f"http://api.sl.se/api2/TravelplannerV3/trip.json?key=&lang=sv&destId=1319\
    &searchForArrival=1"
#search_for_arrival: bool schedule_end: str
# #arrival_true_false = _check_if_search_for_arrival_is_false_or_true(search_for_arrival)
# #schdule_switcher = _start_end_time_switch_(schedule_start, schedule_end, search_for_arrival)
# #search_for_arrival_param = f"&searchForArrival={arrival_true_false}"
def get_trip_from_coordinates(position: str, schedule_start: str):

    coordinates_position_and_arrival_time = position+"&time="+schedule_start
    r = requests.get(url=URL, params=coordinates_position_and_arrival_time)
    return {
        'legs': _get_legs_from_trip(r.json())
    }

def _get_legs_from_trip(data):
    trip = data['Trip'][0]
    legs = [format_leg(l) for l in trip['LegList']['Leg']]
    return legs


def format_leg(leg):
    return {
        'origin': {
            'name': leg['Origin']['name'],
            'time': leg['Origin']['time'],
            'date': leg['Origin']['date']
        },
        'destination': {
            'name': leg['Destination']['name'],
            'time': leg['Destination']['time'],
            'date': leg['Destination']['date']
        },
        'name': leg['name'],
        'type': leg['type']
    }
def _start_end_time_switch_(start, end, arrival):
    if arrival is True:
        return start
    else:
        return end

def _check_if_search_for_arrival_is_false_or_true(arrival):
    if arrival is True:
        return 1
    else:
        return 0
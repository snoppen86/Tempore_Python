from .location import get_coordinates_for_location
from .Slrequest import get_trip_from_coordinates
from .database_inserter import dose_user_exist_in_db, add_user_if_it_dosent_exist_in_db, getting_user_info_by_email
import logging

log = logging.getLogger(__file__)


def main_response_handler(data):
    log.info(f"{data}")
    person = data['person']
    if dose_user_exist_in_db(person):
        travel_plan = getting_user_info_by_email(person)
        return {'Travel plan': travel_plan}
    add_user_if_it_dosent_exist_in_db(person)
    location = get_coordinates_for_location(person['address'])
    commute_travel_plan = get_trip_from_coordinates(location, person['scheduleStart'])
    return {'Travel plan': commute_travel_plan}

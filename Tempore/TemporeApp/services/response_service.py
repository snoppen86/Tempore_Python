from .location import get_coordinates_for_location
from .Slrequest import get_trip_from_coordinates
from .database_inserter import dose_user_exist_in_db, add_user_if_it_dosent_exist_in_db, getting_user_info_by_email
import datetime
from TemporeApp import views
import logging

log = logging.getLogger(__file__)
tday = datetime.date.today()


def main_response_handler(data):
    log.info(f"{data}")
    person = data['person']
    travel_response = _travel_response_handler(person)
    return travel_response


def _travel_response_handler(person):
    if dose_user_exist_in_db(person):
        travel_plan = getting_user_info_by_email(person)
        return {'Travel plan': travel_plan}
    add_user_if_it_dosent_exist_in_db(person)
    location = get_coordinates_for_location(person['address'])
    person_schedule = person['scheduleDays'][str(tday.isoweekday())]
    commute_travel_plan = get_trip_from_coordinates(location, person_schedule)
    return {'Travel plan': commute_travel_plan}

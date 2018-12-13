import pymongo
from Tempore import settings
import logging
from .location import get_coordinates_for_location
from .Slrequest import get_trip_from_coordinates
log = logging.getLogger(__file__)
db = pymongo.MongoClient(settings.MONGODB_URI, connect=False)
accounts = db['Accounts']
user_col = accounts['users']


def dose_user_exist_in_db(person):
    user = person
    if user_col.find_one({'email': user['email']}):
        log.debug("getting user info by email")
        return True


def add_user_if_it_dosent_exist_in_db(person):
    log.debug("new user created")
    user_col.insert_one(person)
    return False


def getting_user_info_by_email(person):
    log.debug(user_col.find_one(person))
    person_info = user_col.find_one(person)
    location = get_coordinates_for_location(person_info['address'])
    commute_travel_plan = get_trip_from_coordinates(location, person_info['scheduleStart'])
    return commute_travel_plan

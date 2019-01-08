import pymongo
from Tempore import settings
import logging
from .location import get_coordinates_for_location
from .Slrequest import get_trip_from_coordinates
import datetime

log = logging.getLogger(__file__)
db = pymongo.MongoClient(settings.MONGODB_URI, connect=False)
accounts = db['Accounts']
user_col = accounts['users']
tday = datetime.date.today()


def dose_user_exist_in_db(person):
    user = person
    if user_col.find_one({'email': user['email']}):
        log.debug("getting user info by email")
        return True


def add_user_if_it_dosent_exist_in_db(person):
    if person['address'] and person['scheduleDays'][str(tday.isoweekday())] is None:
        log.warning("You are missing some arguments", exc_info=True)
    log.debug("new user created")
    user_col.insert_one(person)


def getting_user_info_by_email(person):
    log.debug(user_col.find_one({'email': person['email']}))
    person_info = user_col.find_one({'email': person['email']})
    location = get_coordinates_for_location(person_info['address'])
    commute_travel_plan = get_trip_from_coordinates(location, person_info['scheduleDays'][str(tday.isoweekday())] \
        ['scheduleStart'])
    return commute_travel_plan

def update_user_info(client_person):
    user_col.find_one_and_update(client_person)




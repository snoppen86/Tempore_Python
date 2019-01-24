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


def add_user_if_it_dosent_exist_in_db(data):
    if data['address'] and data[str(tday.isoweekday())]is None:
        log.warning("You are missing some arguments", exc_info=True)
    log.debug("new user created")
    user = {
        'Name': data['Name'],
        'email': data['email'],
        'address': data['address'],
        '1': data['1'],
        '2': data['2'],
        '3': data['3'],
        '4': data['4'],
        '5': data['5']
    }
    user_col.insert_one(user)


def getting_user_info_by_email(data):
    log.debug(user_col.find_one({'email': data['email']}))
    person_info = user_col.find_one({'email': data['email']})
    location = get_coordinates_for_location(person_info['address'])
    commute_travel_plan = get_trip_from_coordinates(location, person_info[str(tday.isoweekday())])
    return commute_travel_plan


def update_user_info(client_person):
    user_col.find_one_and_update(client_person)




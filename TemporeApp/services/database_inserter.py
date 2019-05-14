import pymongo
from Tempore import settings
import logging
from .location import get_coordinates_for_location
from .Slrequest import get_trip_from_coordinates
import datetime

log = logging.getLogger(__file__)
db = pymongo.MongoClient(settings.MONGODB_URL, connect=True)
accounts = db['Accounts']
user_col = accounts['users']
tday = datetime.date.today()
realtime = datetime.datetime.now()


def dose_user_exist_in_db(person):
    user = _get_user_data(person)
    if user_col.find_one({'email': user['email'].lower()}):
        log.debug("getting user info by email")
        return True
    return False


def upsert_user_info(data):
    if dose_user_exist_in_db(data) is True:
        user_col.update_one({'email': data['email']}, {"$set":  {'email': data['email']}}, upsert=True)

# str(tday.isoweekday())
def add_user_if_it_dosent_exist_in_db(data):
    if data['address'] and data['1']is None:
        log.warning("You are missing some arguments", exc_info=True)
    log.debug("new user created")
    user = _get_user_data(data)
    user_col.insert_one(user)

def _get_user_data(data):
    return {
        'Name': data['Name'],
        'email': data['email'].lower(),
        'address': data['address'],
        '1': data['1'],
        '2': data['2'],
        '3': data['3'],
        '4': data['4'],
        '5': data['5']
    }

def getting_user_info_by_email(data):
    log.info(user_col.find_one({'email': data['email'].lower()}))
    person_info = user_col.find_one({'email': data['email'].lower()})
    location = get_coordinates_for_location(person_info['address'])
    #Getting person data for the next day after 18:00
    if int(realtime.strftime('%H')) >= 18:
        commute_travel_plan = get_trip_from_coordinates(location, person_info[str(tday.isoweekday()+1)])
        return commute_travel_plan
    #Getting today's travel plan for the client
    commute_travel_plan = get_trip_from_coordinates(location, person_info[str(tday.isoweekday())])
    return commute_travel_plan

# str(tday.isoweekday())



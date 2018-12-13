import pymongo
from Tempore import settings

db = pymongo.MongoClient(settings.MONGODB_URI, connect=False)
accounts = db['Accounts']
user_col = accounts['users']


def dose_user_exist_in_db(person):
    user = person
    if user_col.find_one({'email': user['email']}):
        print("Existing Person ")
        return True


def add_user_if_it_dosent_exist_in_db(person):
    print("new user created")
    user_col.insert_one(person)
    return False

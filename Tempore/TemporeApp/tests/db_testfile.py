import pymongo
import os
#MONGODB_URI = os.environ.get('MONGODB_URI', "mongodb://localhost:27017/")
db = pymongo.MongoClient("mongodb://localhost:27017/")

testJson = {"name":"scott", "email":"bajs@bajs.se"}
testJson1 = {"name":"asdas", "email":"basdajs@baasdasdjs.com"}
userDB = db['userDataBase']
userCol = userDB['users']
if userCol.find_one({"email": testJson1['email']}):
    print("found")
else:
    print("new user created")
    userCol.insert_one(testJson1)

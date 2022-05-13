from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.exception import AppwriteException
import creds
import collections

client = Client()

(client
 .set_endpoint(creds.endpoint)  # Your API Endpoint
 .set_project(creds.project_id)  # Your project ID
 .set_key(creds.api_secret)  # Your secret API key
 # .set_self_signed()  # Use only on dev mode with a self-signed SSL cert
 )


def makeUser(id, name):
    print(id, name)
    users = Users(client)
    result = users.create(user_id=str(id), name=name,
                          email=f"{id}@topo.com", password=str(id)+"1234567890")
    users.update_prefs(str(id), {'points': 0})


def checkExistence(id):
    ids = []
    users = Users(client)
    for user in users.list()['users']:
        ids.append(user['$id'])
    if str(id) in ids:
        return True
    else:
        return False


def updateScore(id, points):
    users = Users(client)
    curr_points = 0
    for user in users.list()['users']:
        if user['$id'] == str(id):
            curr_points = user['prefs']['points']
    result = users.update_prefs(str(id), {'points': curr_points+points})


def leaderBoard():
    leaderboard = dict()
    users = Users(client)
    for user in users.list()['users']:
        leaderboard[user['name']] = user['prefs']['points']
    sorted_leaderboard = collections.OrderedDict(leaderboard)
    return dict(sorted_leaderboard)

def checkScore(id):
    users = Users(client)
    for user in users.list()['users']:
        if user['$id'] == str(id):
            return user['prefs']['points']    


# print(leaderBoard())

# https://appwrite.io/docs/server/database?sdk=python-default
# work on this
# economy system
# host website on heroku bot will run locally 24/7 along with appwrite server on pc
# shift to a pendrive OPTIONAL
# make local api which can display leaderboard from appwrite data and show on ip
# and make bot request data from this local api
# for appwriote docs refer https://appwrite.io/docs/server/account?sdk=python-default

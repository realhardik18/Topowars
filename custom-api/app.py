from flask import Flask, render_template, request
from threading import Thread
from appwrite.client import Client
from appwrite.services.users import Users
import creds
import collections
client = Client()

(client
 .set_endpoint(creds.endpoint)  # Your API Endpoint
 .set_project(creds.project_id)  # Your project ID
 .set_key(creds.api_secret)  # Your secret API key
 # .set_self_signed()  # Use only on dev mode with a self-signed SSL cert
 )

app = Flask('')


@app.route('/')
def home():
    leaderboard = dict()
    users = Users(client)
    for user in users.list()['users']:
        leaderboard[user['name']] = user['prefs']['points']
    sorted_leaderboard = collections.OrderedDict(leaderboard)
    return dict(sorted_leaderboard)
    # cuatom


def run():
    app.run(host='0.0.0.0', debug=True)


def show_site():
    t = Thread(target=run)
    t.start()


run()
# show user stats
# country stats
# home page

# add animations all all nic enice

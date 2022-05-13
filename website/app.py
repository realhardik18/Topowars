from flask import Flask, render_template, request
from threading import Thread
import requests
import creds
import json
app = Flask('')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/leaderboard')
def leaderboard():
    response = requests.get(creds.api_endpoint)
    data = response.text
    return render_template("leaderboard.html", data=response.text)


@app.route('/commands')
def commands():
    return render_template("commands.html")


# show user stats
# country stats
# home page

# add animations all all nic enice

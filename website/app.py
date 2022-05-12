from flask import Flask, render_template, request
from threading import Thread
import requests

app = Flask('')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")


@app.route('/commands')
def commands():
    return render_template("commands.html")


def run():
    app.run()


run()
# show user stats
# country stats
# home page

# add animations all all nic enice

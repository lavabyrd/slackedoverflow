from application import app
from flask import Flask, request, json, jsonify, make_response, render_template, url_for, redirect, flash
from flask_login import current_user, login_user
from application.models import User
from slackclient import SlackClient

import application.actions_logic
import application.misc_func
import application.Oauth_logic

# from config import Config

# Allows pretty printing of json to console
import application.json_format
import os
# Creation of the Flask app
# app = Flask(__name__)
# app.config.from_object(Config)

b_token = app.config['BOT_TOKEN']
u_token = app.config['USER_TOKEN']
veri = app.config['VERIFICATION_TOKEN']
oauth_scope = app.config['OAUTH_SCOPE']
client_id = app.config['CLIENT_ID']
client_secret = app.config['CLIENT_SECRET']


# Global reference for the Slack Client tokens
sc = SlackClient(b_token)
sc_user = SlackClient(u_token)


# Main index page
@app.route("/")
def index():
    return render_template('index.html')


# login page for testing
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # haven't implemented this yet...
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user is None or not user.check_password(form.password.data):
    #         flash('Invalid username or password')
    #         return redirect(url_for('login'))
    #     login_user(user, remember=form.remember_me.data)
    #     return redirect(url_for('index'))
    # return render_template('login.html', form=form)
    return render_template('login.html')


# this returns to both the browser and also to slack
@app.route("/ping", methods=["GET", "POST"])
def ping_slackside_endpoint():
    if request.method == "POST":
        application.misc_func.ping()
        return make_response("pong",
                             200
                             )
    else:
        return "pong"


# this needs to be fixed as currently the logic is broken
@app.route("/actions", methods=["POST"])
def actions():
    payload = json.loads(request.form.get("payload"))
    if payload["token"] == veri:
        print("payload token ok")
        if payload["callback_id"] == "threadDis":
            print("payload callback ok")
            ts = payload["message"]["ts"]
            channel_id = payload["channel"]["id"]
            user_id = payload["user"]["id"]
            application.misc_func.thread_info(channel_id, ts)
            return make_response("OK", 200)
        else:
            return make_response("wrong token, who dis", 403)

    application.actions_logic.action_calling(payload)


# Oauth install endpoint
@app.route("/oauth_install", methods=["GET"])
def pre_install():

    # This shall be split out to a template shortly
    return render_template("install_so.html",
                           oauth_scope=oauth_scope,
                           client_id=client_id
                           )


# Oauth finished endpoint
@app.route("/oauth_completed", methods=["GET", "POST"])
def post_install():
    auth_response = application.Oauth_logic.oauth_access()
    return f"Authed and installed to your team - {auth_response['team_name']}"


# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))

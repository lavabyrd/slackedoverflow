import os
from flask import Flask, request, json, jsonify, make_response, render_template
from slackclient import SlackClient

import actions_logic
import misc_func
from config import Config

# Allows pretty printing of json to console
import json_format

# Creation of the Flask app
app = Flask(__name__)
app.config.from_object(Config)

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


# this returns to both the browser and also to slack
@app.route("/ping", methods=["GET", "POST"])
def ping_slackside_endpoint():
    if request.method == "POST":
        misc_func.ping()
        return make_response("pong", 200)
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
            misc_func.thread_info(channel_id, ts)
            return make_response("OK", 200)
        else:
            return make_response("wrong token, who dis", 403)

    actions_logic.action_calling(payload)


# Oauth install endpoint
@app.route("/oauth_install", methods=["GET"])
def pre_install():

    # This shall be split out to a template shortly
    return f'''
      <a href="https://slack.com/oauth/authorize?scope={oauth_scope}&client_id={client_id}">
          <img alt="Add to Slack" height="40" width="139" src="
          https://platform.slack-edge.com/img/add_to_slack.png"
          srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x,
          https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" />
      </a>
  '''


# Oauth finished endpoint
@app.route("/oauth_completed", methods=["GET", "POST"])
def post_install():

    # Retrieve the authentication code from the request
    auth_code = request.args['code']

    # Request the authentication tokens from Slack
    auth_response = sc.api_call(
        "oauth.access",
        client_id=client_id,
        client_secret=client_secret,
        code=auth_code
    )
    os.environ["SO_USER_TOKEN"] = auth_response['access_token']
    print(f"the team_id is {auth_response['team_id']}")
    return f"Authed and installed to your team - {auth_response['team_name']}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(debug=False, host="0.0.0.0", port=port)

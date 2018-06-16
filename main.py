import os
from flask import Flask, request, json, jsonify, make_response, render_template
from slackclient import SlackClient

from actions_logic import *

from config import Config

# Allows pretty printing of json to console
import json_format

# Creation of the Flask app
app = Flask(__name__)
app.config.from_object(Config)

b_token = app.config['BOT_TOKEN']
u_token = app.config['USER_TOKEN']
veri = app.config['VERIFICATION_TOKEN']

# Global reference for the Slack Client tokens
sc = SlackClient(b_token)
sc_user = SlackClient(u_token)

# Points to the index page and just shows an easy way to
# determine the site is up


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/ping", methods=["POST", "GET"])
def ping_endpoint():
    sc.api_call("chat.postMessage", channel="CB7B4J8F3",
                text="server pinged!", as_user="true")
    return make_response("pong", 200)


def thread_info(channel_id, ts):
    payload = sc.api_call('conversations.replies',
                          channel=channel_id, ts=ts)
    print(json_format.pretty_json(payload))


@app.route("/actions", methods=["POST"])
def actions():
    payload = json.loads(request.form.get("payload"))
    action_calling(payload)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(debug=False, host="0.0.0.0", port=port)

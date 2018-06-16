import os
from flask import Flask, request, json, jsonify, make_response, render_template
from slackclient import SlackClient

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

# Endpoint for the slash command


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
    """
    action endpoint, receiving payloads when user clicks the action
    grabbing the relevant values and parsing the reactions
    """
    payload = json.loads(request.form.get("payload"))
    # print(json_format.pretty_json(payload))
    ts = payload["message"]["ts"]
    channel_id = payload["channel"]["id"]
    thread_info(channel_id, ts)
    # this will be swapped to use the env variable
    if payload["token"] == veri:
        print("payload token ok")
        if payload["callback_id"] == "threadDis":
            print("payload callback ok")
            ts = payload["message"]["ts"]
            channel_id = payload["channel"]["id"]
            user_id = payload["user"]["id"]
            thread_info(channel_id, ts)
        return make_response("OK", 200)
    else:
        return make_response("wrong token, who dis", 403)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(debug=False, host="0.0.0.0", port=port)

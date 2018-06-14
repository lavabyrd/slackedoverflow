import os
from flask import Flask, request, json, jsonify, make_response, render_template
from slackclient import SlackClient

# Allows pretty printing of json to console
import json_format


# Addition of the tokens required. User_token may not be
# needed here unless we want to kick a user from the channel
VERIFICATION_TOKEN = os.environ.get("SO_VERIFICATION_TOKEN")

BOT_TOKEN = os.environ.get("SO_TOKEN")
# I may not need a user token here. The scope should be ok
USER_TOKEN = os.environ.get("SO_USER_TOKEN")

veri = "Np65upwbjYikrfb5HpiV7305"
# Creation of the Flask app
app = Flask(__name__)

# Global reference for the Slack Client tokens
sc = SlackClient(BOT_TOKEN)
sc_user = SlackClient(USER_TOKEN)

# Points to the index page and just shows an easy way to
# determine the site is up


@app.route("/")
def index():
    return render_template('index.html')

# Endpoint for the slash command


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
    user_id = payload["user"]["id"]
    thread_info(channel_id, ts)
    # this will be swapped to use the env variable
    if payload["token"] == veri:
        if payload["callback_id"] == "threadDis":
            ts = payload["message"]["ts"]
            channel_id = payload["channel"]["id"]
            user_id = payload["user"]["id"]
            thread_info(channel_id, ts)
        return make_response("OK", 200)
    else:
        return make_response("wrong token, who dis", 403)


@app.route("/SO", methods=["POST"])
def glow():
    payload = request.form.to_dict()
    print(json_format.pretty_json(payload))
    channel_id = payload["channel_id"]
    user_list = sc.api_call("conversations.members", channel=channel_id)
    print(user_list)
    return make_response("starting the glow!", 200)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(debug=False, host="0.0.0.0", port=port)

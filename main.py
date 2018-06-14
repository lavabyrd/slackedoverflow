import os
from flask import Flask, request, json, jsonify, make_response, render_template
from slackclient import SlackClient

import pymongo
from pymongo import MongoClient
# Allows pretty printing of json to console
import json_format
import glow_logic

# Addition of the tokens required. User_token may not be
# needed here unless we want to kick a user from the channel
VERIFICATION_TOKEN = os.environ.get("GLOW_VERIFICATION_TOKEN")
BOT_TOKEN = os.environ.get("GLOW_BOT_TOKEN")
USER_TOKEN = os.environ.get("GLOW_USER_TOKEN")
MONGODBURL = os.environ.get("MONGO_URL")
# Creation of the Flask app
app = Flask(__name__)

# mongodb://<dbuser>:<dbpassword>@ds259250.mlab.com:59250/glow_worm_staging
client = MongoClient('ds259250.mlab.com', 59250)
db = client['glow_worm_staging']
db.authenticate('dbrwuser', 'Nok1a45de')
# Global reference for the Slack Client tokens
sc = SlackClient(BOT_TOKEN)
sc_user = SlackClient(USER_TOKEN)

# Points to the index page and just shows an easy way to
# determine the site is up


@app.route("/")
def index():
    collection = db['staging_messages']
    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"]}
    posts = db.staging_messages
    post_id = posts.insert_one(post).inserted_id
    print(f"blah here's the post id - {post_id}")
    return render_template('index.html')

# Endpoint for the slash command


@app.route("/glow", methods=["POST"])
def glow():
    payload = request.form.to_dict()
    print(json_format.pretty_json(payload))
    channel_id = payload["channel_id"]
    user_list = sc.api_call("conversations.members", channel=channel_id)
    glow_logic.user_iteration(user_list)
    return make_response("starting the glow!", 200)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(debug=False, host="0.0.0.0", port=port)

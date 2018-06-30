import app.routes
import app.json_format
from flask import json, request, make_response


def thread_info(channel_id, ts):
    payload = app.routes.sc.api_call('conversations.replies',
                                     channel=channel_id, ts=ts)
    print(json_format.pretty_json(payload))


def ping():
    target_channel = json.dumps(request.form['channel_id'])
    app.routes.sc.api_call("chat.postMessage", channel=target_channel,
                           text="pong!", as_user="true")

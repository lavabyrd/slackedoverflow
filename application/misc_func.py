from application import (
    json_format,
    routes
)
from flask import (
    json,
    make_response,
    request
)


def thread_info(channel_id, ts):
    payload = routes.sc.api_call('conversations.replies',
                                 channel=channel_id, ts=ts)
    print(json_format.pretty_json(payload))


def ping():
    target_channel = json.dumps(request.form['channel_id'])
    routes.sc.api_call("chat.postMessage", channel=target_channel,
                       text="pong!", as_user="true")

import application.routes
from flask import make_response
import application.misc_func


def action_calling(payload):
    """
        action endpoint, receiving payloads when user clicks the action
        grabbing the relevant values and parsing the reactions
    """

    # print(json_format.pretty_json(payload))
    ts = payload["message"]["ts"]
    channel_id = payload["channel"]["id"]
    application.misc_func.thread_info(channel_id, ts)
    if payload["token"] == application.routes.veri:
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


def action_calling(payload):
    """
        action endpoint, receiving payloads when user clicks the action
        grabbing the relevant values and parsing the reactions
        """

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

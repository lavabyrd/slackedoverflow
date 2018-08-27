import copy

from flask import (
    Flask,
    json,
    jsonify,
    make_response
)

from config import Config

from application import (
    app,
    misc_func,
    routes
)
from tasks import make_celery

app = Flask(__name__)
app.config.from_object(Config)
celery = make_celery(app)


@celery.task
def action_calling(payload, veri):
    """
        action endpoint, receiving payloads when user clicks the action
        grabbing the relevant values and parsing the reactions
    """
    p1 = json.loads(payload)
    p = copy.deepcopy(p1)
    print(type(p))
    # payload = jsonify(payload).text
    if p["token"] == veri:
        # debug checking of payload token
        # print("payload token ok")
        if p["callback_id"] == "threadDis":
            # Uncomment to check the payload token is valid
            # print("payload callback ok")
            ts = p["message"]["ts"]
            team_id = p["team"]["id"]
            team_domain = p["team"]["domain"]
            channel_id = p["channel"]["id"]
            user_id = p["user"]["id"]
            print("one")
            # misc_func.post_write(team_id,
            #                      team_domain, user_id, channel_id, ts)
            print("two")
            return make_response("OK", 200)
        else:
            return make_response("wrong token, who dis", 403)

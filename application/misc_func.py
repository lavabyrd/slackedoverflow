from application import (
    json_format,
    routes
)

from flask import (
    json,
    make_response,
    request
)

from application import models


def thread_info(channel_id, ts):
    payload = routes.sc_user.api_call('conversations.replies',
                                      channel=channel_id, ts=ts)
    return payload['messages']


def ping():
    target_channel = json.dumps(request.form['channel_id'])
    routes.sc.api_call("chat.postMessage", channel=target_channel,
                       text="pong!", as_user="true")


# post_write(output_post, ts, team_id, team_domain, user_id)
# user = models.User(username=form.username.data, email=form.email.data)
    # user.set_password(form.password.data)
    # db.session.add(user)
    # db.session.commit()
def post_write(team_id, team_domain, user_id, channel_id, ts):
    print("step1")

    for i in thread_info(channel_id, ts):
        post = models.Post(
            message_text=i['text'],
            team_id=team_id,
            team_domain=team_domain,
            user_added=user_id
        )
        print(i['text'])

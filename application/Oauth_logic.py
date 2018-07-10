import os
from application import routes
from flask import request


def oauth_access():
    # Retrieve the authentication code from the request
    auth_code = request.args['code']

    # Request the authentication tokens from Slack
    auth_response = application.routes.sc.api_call(
        "oauth.access",
        client_id=application.routes.client_id,
        client_secret=application.routes.client_secret,
        code=auth_code
    )
    os.environ["SO_USER_TOKEN"] = auth_response['access_token']
    print(f"the team_id is {auth_response['team_id']}")
    return auth_response

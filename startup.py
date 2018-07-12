from application import (
    app,
    db,
    models
)
import os


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': models.User, 'Post': models.Post}


# this may not be required as I'm using a top level entry point

# App startup
# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))

#     app.run(debug=False,
#             host="0.0.0.0",
#             port=port
#             )

port = int(os.environ.get('PORT', 5000))

app.run(debug=False,
        host="0.0.0.0",
        port=port
        )

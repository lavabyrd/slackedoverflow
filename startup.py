from application import app, db
import os
from application.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


# App startup
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.run(debug=False,
            host="0.0.0.0",
            port=port
            )

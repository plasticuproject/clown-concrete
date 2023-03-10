"""wsgi.py"""

import os
from app import app

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=os.environ.get("FLASK_SERVER_PORT"),
        # ssl_context='adhoc',
        # port=443,
        debug=False,
    )

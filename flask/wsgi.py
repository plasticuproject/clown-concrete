"""wsgi.py"""
from __future__ import annotations
import os
from app import app

PORT: int | None
GET_PORT = os.environ.get("FLASK_SERVER_PORT")
if GET_PORT and GET_PORT.isdigit():
    PORT = int(GET_PORT)
else:
    PORT = None

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=PORT,
        # ssl_context="adhoc",
        # port=443,
        debug=False,
    )

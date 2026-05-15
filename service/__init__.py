from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

Talisman(
    app,
    force_https=False,
    content_security_policy={
        'default-src': "'self'"
    }
)

CORS(app)

from service import routes  # noqa: F401, E402
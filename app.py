from flask import Flask, current_app, app
from api.api import api_blueprint
from main.views import main_blueprint
import logging


logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from majestoc_resa.services import api
# from majestoc_resa.services import blueprint


app = Flask(__name__)

# the API-versioned way
# app.register_blueprint(blueprint, url_prefix='/api/1')

# the regular way
api.init_app(app)
app.run(debug=True)

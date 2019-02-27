from flask import Blueprint
from flask_restplus import Api
from .film_service import api as films_api

# if using the blueprint for API versionning (overkill for now)
# blueprint = Blueprint('api', __name__)
# api = Api(blueprint, title='Majestoc REST API', version='1.0', description='API de developpement')


api = Api(title='Majestoc REST API', version='1.0', description='API de developpement')
api.add_namespace(films_api)

from flask_restplus import Api
from .film_service import api as films_api

api = Api(title='Majestoc REST API', version='1.0', description='API de developpement')
api.add_namespace(films_api)

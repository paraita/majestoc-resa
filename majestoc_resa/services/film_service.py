from flask_restplus import Resource, Namespace

from majestoc_resa.model import Film

api = Namespace('films', description='Les films')


@api.route('/')
class FilmService(Resource):
    def get(self):
        films = [{'titre': c.film_nom, 'duree': c.film_duree} for c in Film.query.all()]
        return films

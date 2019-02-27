from flask_restplus import Resource, Namespace

api = Namespace('films', description='Les films')

LIST_FILMS = [
    {'nom': 'Star Wars Un Nouvel Espoir', 'duree': 120},
    {'nom': "Star Wars l'empire contre attaque", 'duree': 140}
]


@api.route('/')
class FilmService(Resource):
    def get(self):
        return LIST_FILMS

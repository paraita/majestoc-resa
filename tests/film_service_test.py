import unittest
from majestoc_resa.services.film_service import FilmService


class TestFilmService(unittest.TestCase):

    EXPECTED_LIST_FILMS = [
        {'nom': 'Star Wars Un Nouvel Espoir', 'duree': 120},
        {'nom': "Star Wars l'empire contre attaque", 'duree': 140}
    ]

    def test_get_all_movies(self):
        filmService = FilmService()
        self.assertEqual(filmService.get(), self.EXPECTED_LIST_FILMS)

import unittest
from majestoc_resa.services.film_service import FilmService
from unittest.mock import patch, Mock


def build_film(nom, duree):
    film = Mock()
    film.film_nom = nom
    film.film_duree = duree
    film.return_value = {'titre': nom, 'duree': duree}
    return film


class TestFilmService(unittest.TestCase):

    EXPECTED_LIST_FILMS = [
        {'titre': 'Star Wars un nouvel espoir', 'duree': 120},
        {'titre': "Star Wars l'empire contre attaque", 'duree': 260}
    ]

    @patch('majestoc_resa.services.film_service.Film')
    def test_get_all_movies(self, client_mock):
        client_mock.query.all.return_value = [build_film(f['titre'], f['duree']) for f in self.EXPECTED_LIST_FILMS]
        service = FilmService()
        self.assertEqual(service.get(), self.EXPECTED_LIST_FILMS)

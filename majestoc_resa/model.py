from . import db


class Seance(db.Model):
    """Item du planning des séances"""
    pass


class Film(db.Model):
    """Modele d'un film avec son nom et sa durée"""
    pass


class Salle(db.Model):
    """Item du planning des salles"""
    pass


class Resa(db.Model):
    """Materialise une réservation de séance"""
    pass


# Est-ce qu'il faut un compte ?
# class User(db.Model):
#     """Il faut un compte afin de pouvoir réserver une place de cinéma"""
#     pass

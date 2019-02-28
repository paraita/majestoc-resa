from . import db


class Seance(db.Model):
    """Item du planning des séances"""
    def __init__(self, id_sceance, film, date_debut, date_fin, duree_sceance):
        self.id_sceance = id_sceance
        self.film = film
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.duree_sceance = duree_sceance
    pass


class Film(db.Model):
    """Modele d'un film avec son nom et sa durée"""
    def __init__(self, nom, duree, sypnosis):
        self.nom = nom
        self.duree = duree
        self.sypnosis = sypnosis
    pass


class Salle(db.Model):
    """Item du planning des salles"""
    def __init__(self, cinema, numero_salle, capacite_salle, numero_siege):
        self.cinema = cinema
        self.numero_salle = numero_salle
        self.capacite_salle = capacite_salle
        self.numero_siege = numero_siege
    pass


class Resa(db.Model):
    """Materialise une réservation de séance"""
    def __init__(self, nom_client, prenom_client, siege_reserver):
        self.nom_client = nom_client
        self.prenom_client = prenom_client
        self.siege_reserver = siege_reserver
    pass

# Est-ce qu'il faut un compte ?
# class User(db.Model):
#     """Il faut un compte afin de pouvoir réserver une place de cinéma"""
#     pass

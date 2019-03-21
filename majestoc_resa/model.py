from sqlalchemy.orm import relationship

from . import db
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime


# db.metadata.clear()


class Film(db.Model):
    """Modele d'un film avec son nom et sa durée (en minutes)"""
    __tablename__ = 'film'
    __mapper_args__ = {'column_prefix': 'film_'}
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    nom = Column(String, nullable=False, unique=False)
    duree = Column(Integer, nullable=False, unique=False)


class Seance(db.Model):
    """Item du planning des séances"""
    __tablename__ = 'seance'
    __mapper_args__ = {'column_prefix': 'seance_'}
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    film = Column(Integer, ForeignKey('film.id'))
    debut = Column(DateTime, nullable=False, unique=False)
    fin = Column(DateTime, nullable=False, unique=False)
    duree = Column(Integer, nullable=False, unique=False)
    cinema = Column(Integer, ForeignKey('cinema.id'))


class Place(db.Model):
    """Une place dans une salle de cinéma"""
    __tablename__ = 'place'
    __mapper_args__ = {'column_prefix': 'place_'}
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    nom = Column(String, nullable=False, unique=False)
    salle = Column(Integer, ForeignKey('salle.id'))


class Salle(db.Model):
    """Item du planning des salles"""
    __tablename__ = 'salle'
    __mapper_args__ = {'column_prefix': 'salle_'}
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    cinema = Column(Integer, ForeignKey('cinema.id'), nullable=False)
    nom = Column(String, nullable=False, unique=False)
    capacite = Column(Integer, nullable=False, unique=False)
    places = relationship('Place')


class Cinema(db.Model):
    """Un cinéma possède des salles qui projetent des films"""
    __tablename__ = 'cinema'
    __mapper_args__ = {'column_prefix': 'cinema_'}
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    nom = Column(String, nullable=False, unique=False)
    salles = relationship('Salle')
    seances = relationship('Seance')


class Reservation(db.Model):
    """Une réservation lie une place, une séance et un client"""
    __tablename__ = 'reservation'
    __mapper_args__ = {'column_prefix': 'resa_'}
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    client = Column(Integer, ForeignKey('client.id'))
    siege = Column(Integer, ForeignKey('place.id'))
    seance = Column(Integer, ForeignKey('seance.id'))


class Client(db.Model):
    __tablename__ = 'client'
    __mapper_args__ = {'column_prefix': 'client_'}
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    reservations = relationship('Reservation')

# Data Models
from flask import Flask
import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User_Info Entity
class User_Info(db.Model):
    __tablename__ = "user_info"
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.Integer, default=1)
    full_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    tickets = db.relationship("Ticket", cascade="all,delete", backref="user_info", lazy=True)

# Theatre Entity
class Theatre(db.Model):
    __tablename__ = "theatre"
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    shows = db.relationship("Show", cascade="all,delete", backref="theatre", lazy=True)

# Show Entity
class Show(db.Model):
    __tablename__ = "show"
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String, nullable=False)
    tags = db.Column(db.String, nullable=False)
    ratings = db.Column(db.Integer, default=0)
    tkt_price = db.Column(db.Float, default=0.0)
    date_time = db.Column(db.DateTime, nullable=False)
    theatre_id = db.Column(db.String, db.ForeignKey("theatre.id"), nullable=False)
    tickets = db.relationship("Ticket", cascade="all,delete", backref="show", lazy=True)

# Ticket Entity
class Ticket(db.Model):
    __tablename__ = "ticket"
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    no_of_tickets = db.Column(db.Integer, nullable=False)
    user_rating = db.Column(db.Integer, default=0)
    sl_nos = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey("user_info.id"), nullable=False)
    show_id = db.Column(db.String, db.ForeignKey("show.id"), nullable=False)
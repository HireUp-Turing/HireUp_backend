from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Text, Boolean
from api import db

class Applicant(db.Model):

    # Is set automatically using class name in lowercase and
    # converted from camelCase to snake_case.
    # Can override with __tablename__
    __tablename__ = 'applicants'

    # The name of the column is the name you assign it to
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(db.String(80))
    last_name = Column(String(80))

    # not sure if this will work:
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now())

    # One to Many Relationship:
    messages = db.relationship('Message', backref='applicant', lazy=True)

class Message(db.Model):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    employer_name = Column(String(100), nullable=False)
    employer_email = Column(String(100), nullable=False)
    body = Column(Text)
    # Enums are complicated; using boolean for now:
    read_status = Column(Boolean, default=False)

    # not sure if this will work:
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now())

    # One to Many Relationship:
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant_id'), nullable=False)

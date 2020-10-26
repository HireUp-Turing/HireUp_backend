from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Text, Boolean
from enum import Enum
from api import db

class ReadStatusEnum(Enum):
    unread = 'unread'
    ignored = 'ignored'
    responded = 'responded'


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

    # Many to Many Relationship:
    applicant_skills = db.relationship('Skill', secondary=applicant_skills, lazy='subquery',
        backref=db.backref('applicants', lazy=True))

# Join Table for Applicants and Skills
applicant_skills = db.Table('applicant_skills',
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True),
    db.Column('applicant_id', db.Integer, db.ForeignKey('applicant.id'), primary_key=True)
)

# Join Table for Applicants and Values
applicant_values = db.Table('applicant_values',
    db.Column('value_id', db.Integer, db.ForeignKey('value.id'), primary_key=True),
    db.Column('applicant_id', db.Integer, db.ForeignKey('applicant.id'), primary_key=True)
)


class Message(db.Model):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    employer_name = Column(String(100), nullable=False)
    employer_email = Column(String(100), nullable=False)
    body = Column(Text)

    # Using Boolean:
    # read_status = Column(Boolean, default=False)

    # Using Enums
    read_status = Column(Enum(ReadStatusEnum),
    default=ReadStatusEnum.unread,
    nullable=False)

    # not sure if this will work:
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now())

    # One to Many Relationship:
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant_id'), nullable=False)


class Skill(db.Model):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    # Many to Many Relationship: nothing needed here.


class Value(db.Model):
    __tablename__ = 'values'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    # Many to Many Relationship: nothing needed here.

from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime
from enum import Enum
from api import db

class Skill(db.Model):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now())

    # Many to Many Relationship: nothing needed here.
    applicants = db.relationship('Applicant', secondary='applicant_skills')

class Value(db.Model):
    __tablename__ = 'values'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now())

    # Many to Many Relationship: nothing needed here.
    applicants = db.relationship('Applicant', secondary='applicant_values')

class ApplicantSkill(db.Model):
    __tablename__ = 'applicant_skills'
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicants.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))

    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now())

    # relationships
    applicant = db.relationship('Applicant', backref=db.backref("applicant_skills", cascade="all, delete-orphan"))
    skill = db.relationship('Skill', backref=db.backref("applicant_skills", cascade="all, delete-orphan"))

class ApplicantValue(db.Model):
    __tablename__ = 'applicant_values'
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicants.id'))
    value_id = db.Column(db.Integer, db.ForeignKey('values.id'))

    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now())

    # relationships
    applicant = db.relationship('Applicant', backref=db.backref("applicant_values", cascade="all, delete-orphan"))
    value = db.relationship('Value', backref=db.backref("applicant_values", cascade="all, delete-orphan"))

class Applicant(db.Model):
    __tablename__ = 'applicants'

    # The name of the column is the name you assign it to
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(db.String(80))
    last_name = Column(String(80))

    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now())

    # One to Many Relationship:
    messages = db.relationship('Message', backref='applicant', lazy=True)

    # Many to Many Relationship:
    skills = db.relationship('Skill', secondary='applicant_skills', lazy='subquery')

    values = db.relationship('Value', secondary='applicant_values', lazy='subquery')

class Message(db.Model):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    employer_name = Column(String(100), nullable=False)
    employer_email = Column(String(100), nullable=False)
    body = Column(Text)

    # Using Boolean:
    read_status = Column(Boolean, default=False)

    # Using Enums
    # read_status = Column(Enum(ReadStatusEnum),
    # default=ReadStatusEnum.unread,
    # nullable=False)

    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now())

    # One to Many Relationship:
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicants.id'), nullable=False)

# This is here in case we get it to work
# class ReadStatusEnum(Enum):
#     unread = 'unread'
#     ignored = 'ignored'
#     responded = 'responded'

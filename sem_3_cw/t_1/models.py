from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum('male', 'female'), nullable=False)
    group = db.Column(db.Enum('A', 'B', 'C'))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'),
nullable=False)

    def __repr__(self):
        return f'Student({self.name}, {self.surname})'

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(80), nullable=False, unique=True)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty {self.faculty_name}'
    

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import func
from dataclasses import dataclass
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.sqlite3"

db = SQLAlchemy(app)
ma = Marshmallow(app)


@dataclass
class Student(db.Model):
    id: int = db.Column("student_id", db.Integer, primary_key=True)
    name: str = db.Column(db.String(100))
    city: str = db.Column(db.String(50))
    addr: str = db.Column(db.String(200))
    pin: str = db.Column(db.String(10))
    enrollment_datetime:datetime = db.Column(db.DateTime(timezone=True), default=func.now())
    last_update:datetime = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

    def __repr__(self):
        return f"<{self.name} lives in {self.city}>"


class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)



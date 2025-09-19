# server/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Integer, Float, String

# (optional) keep MetaData if your course uses it for naming conventions
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model):
    __tablename__ = "earthquakes"

    id = db.Column(Integer, primary_key=True)
    magnitude = db.Column(Float, nullable=False)
    location = db.Column(String, nullable=False)
    year = db.Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"

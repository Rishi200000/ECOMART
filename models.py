# models.py
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Category(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

class Product(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(120), nullable=False)
    price       = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    image       = db.Column(db.String(255))
    si_unit     = db.Column(db.String(50))
    best_before = db.Column(db.Date)
    quantity    = db.Column(db.Integer, default=0)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category.id"),
        nullable=False
    )
    category = db.relationship("Category", backref="products")

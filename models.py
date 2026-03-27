from flask_sqlalchemy import SQLAlchemy
import datetime
import uuid

# DB instance
db = SQLAlchemy()


class Spool(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(120), nullable=False)
    manufacturer = db.Column(db.String(120), nullable=False)   # <- neu
    material = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    total_weight_grams = db.Column(db.Integer, nullable=False)
    remaining_weight_grams = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow,
                           nullable=False)
    archived = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, name, manufacturer, material, color, total_weight_grams, remaining_weight_grams=None, **kwargs):
        self.name = name
        self.manufacturer = manufacturer
        self.material = material
        self.color = color
        self.total_weight_grams = int(total_weight_grams)
        if remaining_weight_grams is None:
            self.remaining_weight_grams = int(total_weight_grams)
        else:
            self.remaining_weight_grams = int(remaining_weight_grams)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "manufacturer": self.manufacturer,   # <- neu
            "material": self.material,
            "color": self.color,
            "total_weight_grams": self.total_weight_grams,
            "remaining_weight_grams": self.remaining_weight_grams,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "archived": self.archived,
        }

    def consume(self, grams):
        grams = int(grams)
        if grams <= 0:
            return 0
        available = self.remaining_weight_grams
        actual = min(grams, available)
        self.remaining_weight_grams = max(0, available - actual)
        return actual

    def refill(self, grams, cap_to_total=True):
        grams = int(grams)
        if grams <= 0:
            return 0
        before = self.remaining_weight_grams
        if cap_to_total:
            self.remaining_weight_grams = min(self.total_weight_grams, before + grams)
        else:
            self.remaining_weight_grams = before + grams
        return self.remaining_weight_grams - before
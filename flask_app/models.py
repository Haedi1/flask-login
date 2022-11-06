"""Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db


class User(UserMixin, db.Model):
    """Model for user accounts."""

    __tablename__ = "flasksession-users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(
        db.String(200), primary_key=False, unique=False, nullable=False
    )
    website = db.Column(db.String(60), index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    # websocket_id = db.Column(db.String, unique=True, index=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.name)


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String())
    sender_id = db.Column(db.String())
    recipient_id = db.Column(db.String())
    subject = db.Column(db.String())
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime)
    read = db.Column(db.Boolean(), default=False)
    thread_id = db.Column(db.String())
    sender_del = db.Column(db.Boolean())
    recipient_del = db.Column(db.Boolean())
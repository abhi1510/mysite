from app import db
from datetime import datetime

DEFAULT_POST_IMG = 'https://images.unsplash.com/photo-1519337265831-281ec6cc8514?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80'
DEFAULT_POST_AUTHOR = 'Abhinav Kumar'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'Post: {self.username}'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, default=DEFAULT_POST_IMG)
    read_time = db.Column(db.Integer, default=5)
    views = db.Column(db.Integer, default=0)
    author = db.Column(db.String(25), default=DEFAULT_POST_AUTHOR)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'Post: {self.title}'


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(50), nullable=True)
    link = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Resource: {self.name}'


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120))
    message = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Message from {self.name}'

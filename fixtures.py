from app import db
from app.config import Config
from app.models import Post, Resource, Contact


NUMBER_OF_POSTS = 30
NUMBER_OF_CONTACTS = 20
NUMBER_OF_RESOURCES = 50


def create_resources():
    for i in range(NUMBER_OF_RESOURCES):
        r = Resource(name=f'Resource {i+1}', description='Python Official docs',
                     link='https://unsplash.com/s/photos/blog', category='python')
        db.session.add(r)
    db.session.commit()
    print(f'{NUMBER_OF_RESOURCES} resources added!')


def create_posts():
    for i in range(NUMBER_OF_POSTS):
        p = Post(title=f'Post title {i+1}', content='Post content')
        db.session.add(p)
    db.session.commit()
    print(f'{NUMBER_OF_POSTS} posts added!')


def create_contacts():
    for i in range(NUMBER_OF_CONTACTS):
        c = Contact(name='John Doe', email='john.doe@gmail.com', subject=Config.CONTACT_SUBJECT,
                    message='This is a test message')
        db.session.add(c)
    db.session.commit()
    print(f'{NUMBER_OF_CONTACTS} contacts added!')


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # create_posts()
    # create_resources()
    # create_contacts()

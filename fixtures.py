from app import db
from app.models import Post, Resource


NUMBER_OF_POSTS = 5
NUMBER_OF_RESOURCES = 20


def create_resources():
    for i in range(NUMBER_OF_RESOURCES):
        r = Resource(name=f'Resource {i+1}', link='https://unsplash.com/s/photos/blog', category='images')
        db.session.add(r)
    db.session.commit()
    print(f'{NUMBER_OF_RESOURCES} resources added!')


def create_posts():
    for i in range(NUMBER_OF_POSTS):
        p = Post(title=f'Post title {i+1}', content='Post content')
        db.session.add(p)
    db.session.commit()
    print(f'{NUMBER_OF_POSTS} posts added!')


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    create_posts()
    create_resources()
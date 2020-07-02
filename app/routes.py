from flask import render_template

from app import app
from app.models import Post, Resource


@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/posts')
def post_list_view():
    posts = Post.query.all()
    return render_template('post-list.html', object_list=posts)


@app.route('/posts/<pk>')
def post_detail_view(pk):
    post = Post.query.get(pk)
    return render_template('post-detail.html', instance=post)


@app.route('/resources')
def resources_view():
    resources = Resource.query.all()
    return render_template('resources.html', object_list=resources)

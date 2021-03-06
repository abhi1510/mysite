from datetime import datetime

from flask import render_template, redirect, flash, url_for, request
from flask_paginate import Pagination, get_page_args
from flask_login import login_user, login_required

from app import app, db
from app.config import Config
from app.models import Post, Resource, Contact, Account
from app.forms import PostForm, ContactForm, ResourceForm, LoginForm


# Main routes

@app.route('/')
def index_view():
    return render_template('main/index.html')


@app.route('/about')
def about_view():
    return render_template('main/about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact_view():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        contact = Contact(name=name, email=email, subject=Config.CONTACT_SUBJECT, message=message)
        db.session.add(contact)
        db.session.commit()
        flash('Your message was sent! Thank You :)', 'success')
        return redirect(url_for('contact_view'))
    return render_template('main/contact.html', form=form)


# Blog routes

@app.route('/posts')
def post_list_view():
    object_list = Post.query.order_by(Post.created_on.desc()).all()
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(object_list)
    paginated_list = object_list[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('blog/post-list.html', object_list=paginated_list, page=page,
                           per_page=per_page, pagination=pagination)


@app.route('/posts/<pk>')
def post_detail_view(pk):
    post = Post.query.get(pk)
    post.views = post.views + 1
    db.session.commit()
    return render_template('blog/post-detail.html', instance=post)


@app.route('/admin/posts/create')
def post_create_view():
    form = PostForm()
    if form.validate_on_submit():
        print(form)
    return render_template('admin/post-form.html', form=form)


# Resources routes

@app.route('/resources')
def resources_view():
    object_list = Resource.query.all()
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(object_list)
    paginated_list = object_list[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('resources.html', object_list=paginated_list, page=page,
                           per_page=per_page, pagination=pagination)


# Admin routes

@app.route('/admin')
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html')


@app.route('/admin/posts')
@login_required
def admin_post_list_view():
    object_list = Post.query.order_by(Post.created_on.desc()).all()
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(object_list)
    paginated_list = object_list[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('admin/posts.html', object_list=paginated_list, page=page,
                           per_page=per_page, pagination=pagination)


@app.route('/admin/posts/create', methods=['GET', 'POST'])
@login_required
def admin_post_create_view():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        image_url = form.image_url.data
        read_time = form.read_time.data
        post = Post(title=title, content=content, image_url=image_url, read_time=read_time)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('admin_post_list_view'))
    return render_template('admin/post-form.html', form=form, title='Create')


@app.route('/admin/posts/<pk>/update', methods=['GET', 'POST'])
@login_required
def admin_post_update_view(pk):
    form = PostForm()
    instance = Post.query.get(pk)
    if form.validate_on_submit():
        instance.title = form.title.data
        instance.content = form.content.data
        instance.image_url = form.image_url.data
        instance.read_time = form.read_time.data
        instance.updated_on = datetime.utcnow()
        db.session.commit()
        flash(f'Post \'{instance.title}\' updated successfully!', 'success')
        return redirect(url_for('admin_post_list_view'))
    elif request.method == 'GET':
        form.title.data = instance.title
        form.content.data = instance.content
        form.image_url.data = instance.image_url
        form.read_time.data = instance.read_time
    return render_template('admin/post-form.html', form=form, instance=instance, title='Update')


@app.route('/admin/posts/<pk>/delete')
@login_required
def admin_post_delete_view(pk):
    instance = Post.query.get(pk)
    db.session.delete(instance)
    db.session.commit()
    flash(f'Post with id {pk} deleted successfully!', 'info')
    return redirect(url_for('admin_post_list_view'))


@app.route('/admin/resources')
@login_required
def admin_resource_list_view():
    object_list = Resource.query.order_by(Resource.created_on.desc()).all()
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(object_list)
    paginated_list = object_list[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('admin/resources.html', object_list=paginated_list, page=page,
                           per_page=per_page, pagination=pagination)


@app.route('/admin/resources/create', methods=['GET', 'POST'])
@login_required
def admin_resource_create_view():
    form = ResourceForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        link = form.link.data
        category = form.category.data
        res = Resource(name=name, description=description, link=link, category=category)
        db.session.add(res)
        db.session.commit()
        flash('Resource created successfully!', 'success')
        return redirect(url_for('admin_resource_list_view'))
    return render_template('admin/resource-form.html', form=form, title='Create')


@app.route('/admin/resources/<pk>/update', methods=['GET', 'POST'])
@login_required
def admin_resource_update_view(pk):
    form = ResourceForm()
    instance = Resource.query.get(pk)
    if form.validate_on_submit():
        instance.name = form.name.data
        instance.description = form.description.data
        instance.link = form.link.data
        instance.category = form.category.data
        db.session.commit()
        flash('Resource updated successfully!', 'success')
        return redirect(url_for('admin_resource_list_view'))
    elif request.method == 'GET':
        form.name.data = instance.name
        form.description.data = instance.description
        form.link.data = instance.link
        form.category.data = instance.category
    return render_template('admin/resource-form.html', form=form, instance=instance, title='Update')


@app.route('/admin/resources/<pk>/delete')
@login_required
def admin_resource_delete_view(pk):
    instance = Resource.query.get(pk)
    db.session.delete(instance)
    db.session.commit()
    flash(f'Resource with id {pk} deleted successfully!', 'info')
    return redirect(url_for('admin_resource_list_view'))


@app.route('/admin/contacts')
@login_required
def admin_contact_list_view():
    object_list = Contact.query.order_by(Contact.created_on.desc()).all()
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(object_list)
    paginated_list = object_list[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('admin/contacts.html', object_list=paginated_list, page=page,
                           per_page=per_page, pagination=pagination)


@app.route('/login', methods=['GET', 'POST'])
def admin_login_view():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Account.query.filter_by(username=username).first()
        if user and user.password == password and user.is_admin:
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('admin/login.html', form=form)

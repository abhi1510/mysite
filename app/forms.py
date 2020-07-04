from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class PostForm(FlaskForm):
    title = StringField('Title*', validators=[DataRequired(), Length(2, 80)])
    content = StringField('Content*', validators=[DataRequired()])
    image_url = StringField('Image URL', validators=[Length(max=300)])
    read_time = IntegerField('Read Time*', validators=[DataRequired()])
    submit = SubmitField('Save Post')


class ResourceForm(FlaskForm):
    name = StringField('Name*', validators=[DataRequired(), Length(max=30)])
    description = StringField('Description*', validators=[DataRequired(), Length(max=50)])
    link = StringField('Link*', validators=[DataRequired()])
    category = StringField('Category*', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Save Resource')


class ContactForm(FlaskForm):
    name = StringField('Your Name*', validators=[DataRequired(), Length(2, 80)])
    email = StringField('Your Email*', validators=[DataRequired(), Email(), Length(5, 120)])
    message = StringField('Your Message*', validators=[DataRequired(), Length(max=300)])
    submit = SubmitField('Submit')

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post = TextAreaField('Pitch', validators=[DataRequired()])
    category = SelectField('Category', choices=[('PRODUCT', 'PRODUCT'), ('INTERVIEW', 'INTERVIEW'), ('PICKUPLINES', 'PICKUPLINES')],
                           validators=[DataRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post')

class Vote(FlaskForm):
    submit = SelectField('Like')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('bio', validators=[DataRequired()])
    submit = SubmitField('Post')

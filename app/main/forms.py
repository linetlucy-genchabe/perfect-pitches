from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post = TextAreaField('Pitch', validators=[DataRequired()])
    category = SelectField('Category', choices=[('PRODUCT', 'PRODUCT'), ('IDEA', 'IDEA'), ('Business', 'Business')],
                           validators=[DataRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post')

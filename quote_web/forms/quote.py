from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class QuoteForm(FlaskForm):
    author = StringField('Автор цитаты', validators=[DataRequired()])
    content = TextAreaField("Цитата")
    submit = SubmitField('Добавить')
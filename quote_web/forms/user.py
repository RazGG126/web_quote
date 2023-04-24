from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=30)])
    surname = StringField('Фамилия', validators=[DataRequired(), Length(min=2, max=30)])
    nick_name = StringField('Имя пользователя', validators=[DataRequired(), Length(min=4, max=20)])
    email = EmailField('Электронная почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=5, max=40)])
    password_again = PasswordField('Подтвердите пароль', validators=[DataRequired(), Length(min=5, max=40)])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Электронная почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
    
    
class ResetPasswordForm(FlaskForm):
    email = EmailField('Электронная почта', validators=[DataRequired()])
    submit = SubmitField('Сбросить пароль')
    

class UpdatePasswordForm(FlaskForm):
    password = PasswordField('Придумайте пароль', validators=[DataRequired(), Length(min=5, max=40)])
    password_again = PasswordField('Подтвердите пароль', validators=[DataRequired(), Length(min=5, max=40)])
    submit = SubmitField('Обновить пароль')

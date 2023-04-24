from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize


class NewNickname(FlaskForm):
    nick_name = StringField('Имя пользователя', validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField('Изменить')


class NewPassword(FlaskForm):
    password = PasswordField('Введите действующий пароль', validators=[DataRequired(), Length(min=5, max=40)])
    password_new = PasswordField('Введите новый пароль', validators=[DataRequired(), Length(min=5, max=40)])
    submit = SubmitField('Обновить пароль')


class ProfilePhoto(FlaskForm):
    photo = FileField("Выберите файл...", validators=[
        FileRequired(), FileAllowed(['jpg', 'png'], 'Запрещенный формат файла.'),
        FileSize(max_size=1048576, message='Максимальный размер файла - 1 Мб.')])
    submit = SubmitField('Загрузить')


class ChangeBlobColor(FlaskForm):
    first_color = StringField('Первый hex цвет', validators=[DataRequired(), Length(min=3, max=6)])
    second_color = StringField('Второй hex цвет', validators=[DataRequired(), Length(min=3, max=6)])
    submit = SubmitField('Перекрасить')
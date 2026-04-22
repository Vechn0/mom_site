from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo,Length

class LoginsForm(FlaskForm):
    username = StringField("Имя пользовавтеля",validators=[DataRequired(message="Имя пользователя"),Length(min=4, max=25)])
    password = PasswordField("Пароль",validators=[DataRequired(message="Пароль"),Length(min=8, max=25)])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegistersForm(FlaskForm):
    username = StringField("Имя пользователя",validators=[DataRequired(message="Имя пользователя"),Length(min=4, max=25)])
    password = PasswordField("Пароль",validators=[DataRequired(message="Пароль"),Length(min=8, max=25)])
    password2 = PasswordField("Подтверждение пароля",validators=[DataRequired(message="Подтверждение пароля"),EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')
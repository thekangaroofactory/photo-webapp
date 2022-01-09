"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Nom',
        validators=[DataRequired()]
    )

    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )

    password = PasswordField(
        'Mot de passe',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )

    confirm = PasswordField(
        'Confirmez le mot de passe',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

    submit = SubmitField('Créer')


class LoginForm(FlaskForm):
    """User Log-in Form."""

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )

    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Connexion')

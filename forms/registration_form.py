from wtforms import Form, StringField, PasswordField, validators


class RegistrationForm(Form):
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=25)
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=6, max=25)
    ])
    confirm = PasswordField('Repeat Password')

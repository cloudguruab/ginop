from wtforms import Form, BooleanField, StringField, PasswordField, validators

class AuthForm(Form): #TODO:
    username = StringField('Username', [validators.Length(min=8, max=25)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class ChainEventsForm(Form):
    pass
from wtforms import Form, StringField, validators


class PostFilterForm(Form):
    q = StringField('Search', [validators.Length(min=1, max=100)])
    title = StringField('Title', [validators.Length(min=1, max=100)])
    body = StringField('Body', [validators.Length(min=1, max=100)])
    userId = StringField('Created By', [validators.Length(min=1, max=100)])
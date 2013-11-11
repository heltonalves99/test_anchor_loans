from wtforms import Form, BooleanField, TextField, TextAreaField, validators
from wtforms import HiddenField

strip_filter = lambda x: x.strip() if x else None

class CommentCreateForm(Form):
    name = TextField('name', [validators.Length(min=1, max=255)],
                      filters=[strip_filter])
    comment = TextAreaField('comment', [validators.Length(min=1)],
                         filters=[strip_filter])

class CommentUpdateForm(CommentCreateForm):
    id = HiddenField()
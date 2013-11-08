# -*- coding: utf-8 -*-
from formencode import Schema, validators


class CommentSchema(Schema):

    name = validators.String(not_empty=True, max=254)
    comment = validators.String(not_empty=True)
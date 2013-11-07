# -*- coding: utf-8 -*-
from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home/content.jinja2')
def home(request):

    object_list = request.db['post'].find()
    list_post = []
    for obj in object_list:
		post = {
				"_id": obj[u'_id'],
				"author": obj[u'author'],
				"title": obj[u'title'],
				"content": obj[u'content'][:1000] + '...',
				"date": obj[u'date'].strftime("%B %d %Y"),
				"slug": obj[u'slug']
				}
		list_post.append(post)

    return {'list_post': list_post}

@view_config(route_name='list_post', renderer='templates/base.jinja2')
def list_post(request):
	return {}

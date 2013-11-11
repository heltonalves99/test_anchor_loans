# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from .forms import CommentCreateForm, CommentUpdateForm


def my_view(request):
    return {}

@view_config(route_name='home', renderer='templates/home/content.jinja2')
def home(request):
	# defining numbers of pages and number of posts
	num_list_post = 1
	num_page = 2

	if request.GET.get('page'):
		page = int(request.GET.get('page'))
	else:
		page = 1

	row = num_list_post * (page - 1)
	object_list = request.db['post'].find()[row: row + num_list_post]
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

	# pagination garation
	page_list = []
	for page in range(num_page):
		page_list.append(page + 1)

	return {'list_post': list_post, 'page_list': page_list}

@view_config(route_name='detail_post', renderer='templates/post/detail_post.jinja2')
def detail_post(request, slug):
	slug = slug.matchdict['slug']
	post = request.db['post'].find_one({'slug': slug})

	return {'post': post}

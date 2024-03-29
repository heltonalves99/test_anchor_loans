from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
import pymongo

from test_anchor_loans.resources import Root

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(settings=settings, root_factory=Root,
            session_factory=my_session_factory)

    config.add_view('test_anchor_loans.views.my_view',
                    context='test_anchor_loans:resources.Root',
                    renderer='test_anchor_loans:templates/home/content.jinja2') 
    
    #adding route
    config.add_route('home', '/')
    config.add_route('detail_post', '/list-post/{slug}')

    config.add_static_view('static', 'test_anchor_loans:static')
    # MongoDB
    def add_mongo_db(event):
        settings = event.request.registry.settings
        url = settings['mongodb.url']
        db_name = settings['mongodb.db_name']
        db = settings['mongodb_conn'][db_name]
        event.request.db = db
    db_uri = settings['mongodb.url']
    MongoDB = pymongo.Connection
    if 'pyramid_debugtoolbar' in set(settings.values()):
        class MongoDB(pymongo.Connection):
            def __html__(self):
                return 'MongoDB: <b>{}></b>'.format(self)
    conn = MongoDB(db_uri)
    config.registry.settings['mongodb_conn'] = conn
    config.add_subscriber(add_mongo_db, NewRequest)
    config.include('pyramid_jinja2')
    config.scan('test_anchor_loans')
    return config.make_wsgi_app()

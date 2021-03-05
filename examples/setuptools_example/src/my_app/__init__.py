from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(route_name="index", renderer="string")
def index(request):
    return "Hello, world!"


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route("index", "/")
    config.scan()

    return config.make_wsgi_app()

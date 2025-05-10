from ryu.base import app_manager
from ryu.app.wsgi import WSGIApplication, route, ControllerBase
from webob import Response

class TestRest(app_manager.RyuApp):
    _CONTEXTS = { 'wsgi': WSGIApplication }

    def __init__(self, *args, **kwargs):
        super(TestRest, self).__init__(*args, **kwargs)
        wsgi = kwargs['wsgi']
        wsgi.register(RestController, {})

class RestController(ControllerBase):
    def __init__(self, req, link, data, **configs):
        super(RestController, self).__init__(req, link, data, **configs)

    @route("Test", "/hello/{name}", methods=['GET'])
    def _hello_wsgi(self, req, **kwargs):
        name = kwargs['name']
        print("................")
        print(req)
        print("................")
        return Response(status=200, text=f"Hello {name}")

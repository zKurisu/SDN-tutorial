from ryu.base import app_manager
import logging

logging.basicConfig(level=logging.DEBUG)
class L2Switch(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)
        logging.debug("Hello World")


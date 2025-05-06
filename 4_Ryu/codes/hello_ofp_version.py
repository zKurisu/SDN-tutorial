from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_0
import logging

logging.basicConfig(level=logging.DEBUG)
class L2Switch(app_manager.RyuApp):
    OFP_VERSION = [ofproto_v1_0.OFP_VERSION]
    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)
        logging.debug("Hello World")


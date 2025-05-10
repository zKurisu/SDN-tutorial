from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import set_ev_cls, CONFIG_DISPATCHER
from ryu.ofproto import ofproto_v1_0
import logging

logging.basicConfig(level=logging.DEBUG)

class L2Switch(app_manager.RyuApp):
    OFP_VERSION = ofproto_v1_0
    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)
        logging.debug("Hello Ryu Init!")

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_feature_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        logging.debug(f"In OFP_Switch_Feature: {datapath.id}")


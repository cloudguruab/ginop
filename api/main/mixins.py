"""Custom mixins for ginop api"""
from ..dev.blockchain import chain
from ..dev.blockchain import controller
from ..dev.common import constants
from ..dev.common import exceptions
from ..dev.common import chainTypes

class GinopBlockchainMixin(object):
    
    def begin_work(self, *args, **kwargs):
        pass
    
class ControllerConnectorMixin(object):
    
    def connect(self):
        pass
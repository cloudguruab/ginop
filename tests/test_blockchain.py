from ..api.dev.blockchain import chain
import time
import json
from hashlib import sha256


class TestBlockchain:
    """
    test plan for Block instances and Blockchain instances alike
    """
    
    def setup_method(self):
        self.genesis_block = chain.Block(0, [], time.time(), "0")

    def teardown_method(self):
        self.genesis_block = None
        
    def test_create_genesis_block(self):
        chain_vector = []
        self.genesis_block.hash = self.genesis_block.compute_hash()
        chain_vector.append(self.genesis_block)
        
        assert chain_vector
        assert isinstance(self.genesis_block, object)
        
    
    
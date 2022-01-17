"""types for ginop blockchain logic"""

class BlockTypes:
    """
    configuration for blockchain block types
    
    index: marker for block instances on chain.
    transactions: list of transactions for the chain.
    timestamp: epoch instance for current timestamp of the following chain.
    previous_hash: last hash for most recent block on the chain.
    nonce: arbitrary number when joined with block data forms the hash.
    hash: used for grabbing specifc transactions off a particular block
    """
    index: float or int
    transactions: list
    timestamp: float
    previous_hash: int or float
    nonce: int or float
    
class ChainTypes:
    """
    configuration for blockchain types.
    
    unconfirmed_transactions: list or non-verified transactions on chain
    chain: blockchain vector
    """
    unconfirmed_transactions: list
    chain: list
   
class ControllerTypes:
    """
    configuration for Controller
    
    name: identifier for linked tenant on api
    """
    name: str
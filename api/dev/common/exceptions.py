"""global exceptions for ginop blockchain"""

class ChainConnectionException(Exception):
    """
    handler for failed connections to blockchain platform.
    """

class FailedChainEventExeception(Exception):
    """
    handler for failed blockchain actions on the ginop api.
    """
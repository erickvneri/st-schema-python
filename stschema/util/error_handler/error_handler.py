class ErrorHandler:
    """
    ErrorHandler class to pretty print
    the different exceptions raised through
    development stages.

    Handlers supported:
        - not_implemented_error
    """

    def not_implemented_error(self, origin: str):
        error_msg = '[%s] - Interaction resource handler not implemented' % origin
        raise NotImplementedError(error_msg)

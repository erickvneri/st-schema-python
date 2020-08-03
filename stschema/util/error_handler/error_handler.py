from colorama import Fore

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
        formatted_msg = Fore.RED + error_msg + Fore.RESET
        raise NotImplementedError(formatted_msg)

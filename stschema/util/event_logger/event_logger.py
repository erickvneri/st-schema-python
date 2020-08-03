import logging


class EventLogger:
    def __init__(self, enable: bool):
        self.logger = self._logger(enable)

    def _logger(self, enable):
        logger = logging.getLogger('[stschema]')
        # Handle levels
        logger.setLevel(logging.WARNING)
        if enable:
            logger.setLevel(logging.DEBUG)

        #  Stream handler instance.
        stream  = logging.StreamHandler()
        # Formatter instance
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        stream.setFormatter(formatter)
        logger.addHandler(stream)
        return logger

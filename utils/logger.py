
import logging

class Logger:
    @staticmethod
    def get_logger():
        logger = logging.getLogger("MagentoSignupLogger")
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

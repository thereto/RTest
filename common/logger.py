# 日志封装
import logging

def get_logger():
    logger = logging.getLogger("auto_test")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        )

        console = logging.StreamHandler()
        console.setFormatter(formatter)

        logger.addHandler(console)

    return logger

logger = get_logger()

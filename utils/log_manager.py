import logging
import os
import time


def get_logger(name: str) -> logging.Logger:
    # Create logs directory if not exists
    log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(log_dir, exist_ok=True)

    timestamp = time.strftime("%Y_%m_%d")

    log_file = os.path.join(log_dir, f"orange_hrm_{str(timestamp)}.log")

    # Logger configuration
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # File handle to handle log writing in the log files
    fh = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    fh.setLevel(logging.DEBUG)

    # Console log handler to display logs on console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Log time format
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(fh)
        logger.addFilter(ch)

    return logger
# utils/logger.py
import logging
import os


def setup_logger():
    """Creates a logger that writes to a file, reused across the whole framework"""
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("bagisto_tests")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("logs/test_run.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
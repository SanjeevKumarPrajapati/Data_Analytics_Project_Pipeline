# src/utils.py

import logging
import yaml
import os

def setup_logging(log_file_path='logs/pipeline.log'):
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.handlers.clear()  # Clear existing handlers

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

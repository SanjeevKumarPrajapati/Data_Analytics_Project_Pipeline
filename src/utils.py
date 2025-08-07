# Common utilities (logging, config loader)

import logging
import yaml

def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

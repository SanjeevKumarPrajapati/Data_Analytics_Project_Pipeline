# Orchestrates the pipeline

from src.utils import load_config, setup_logging
from src.data_ingestion import ingest_data
from src.transformation import transform_data
from src.eda import run_eda
import pandas as pd
import logging

def main():
    config = load_config("config/config.yaml")
    setup_logging(config["log_file"])

    logging.info("Pipeline started")

    df = ingest_data(config["data_path"])
    df_cleaned = transform_data(df)
    df_cleaned.to_csv(config["output_path"], index=False)
    logging.info(f"Cleaned data saved to {config['output_path']}")

    run_eda(df_cleaned)

    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    main()

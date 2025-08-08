# Orchestrates the pipeline

from src.utils import load_config, setup_logging
from src.data_ingestion import ingest_data
from src.transformation import transform_data
from src.eda import run_eda
import pandas as pd
import numpy as np
import logging
from src.modeling import modeling

def main():
    config = load_config("config/config.yaml")
    setup_logging(config["log_file"])

    logging.info("Pipeline started............")
    
    logging.info("Data Ingestion started............")
    df = ingest_data(config["data_path"])
    logging.info("Data Ingestion is completed successfully ............")
    
    logging.info("Data Transformation started............")
    df_cleaned = transform_data(df)
    df_cleaned.to_csv(config["output_path"], index=False)
    logging.info(f"Cleaned data saved to {config['output_path']}")
    logging.info("Data Transformation is completed successfully............")
    
    logging.info("Modeling started.......")
    
    modeling(df_cleaned)
    
    logging.info("Exploratory Data Analysis started.........")
    
    run_eda(df_cleaned)

    logging.info("Exploratory Data Analysis is Completed successfully.........")
    
    
    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    main()

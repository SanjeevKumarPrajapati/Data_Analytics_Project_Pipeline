# Exploratory Data Analysis

import logging

def run_eda(df):
    logging.info(f"Shape of data: {df.shape}")
    logging.info(f"Columns: {df.columns.tolist()}")
    logging.info(f"Missing values:\n{df.isnull().sum()}")
    logging.info(f"Descriptive stats:\n{df.describe()}")

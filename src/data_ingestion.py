# Read data from source
import pandas as pd
import logging

df=pd.read_csv("data.csv")
print(df.head())
'''
def ingest_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Data ingested from {file_path} successfully.")
        return df
    except Exception as e:
        logging.error(f"Error ingesting data: {e}")
        raise

ingest_data("data\raw\data.csv")
'''
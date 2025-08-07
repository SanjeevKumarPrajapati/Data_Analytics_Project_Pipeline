# Read data from source
import pandas as pd
import logging


def ingest_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Data ingested from {file_path} successfully.")
        print("Columns : {}".format(df.columns))
        print("\nTotal number of rows and column :- ",df.shape)
        print("\n")
        print("Printing the descriptive information about the data......\n")
        print(df.describe())
        
        
        return df
    except Exception as e:
        logging.error(f"Error ingesting data: {e}")
        raise


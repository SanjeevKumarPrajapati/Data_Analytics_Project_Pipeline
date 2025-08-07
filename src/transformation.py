# Data cleaning and transformation
import logging

def transform_data(df):
    try:
        df.dropna(inplace=True)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        logging.info("Data transformed successfully.")
        return df
    except Exception as e:
        logging.error(f"Error in data transformation: {e}")
        raise

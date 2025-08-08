# Exploratory Data Analysis

import logging

def run_eda(df):
    # Data Structure & Types
    logging.info("Add info about data types and number of unique values.")
    logging.info(f"Data types:\n{df.dtypes}")
    logging.info(f"Unique values per column:\n{df.nunique()}")
    
    #Missing Value Analysis
    missing_info = df.isnull().sum().reset_index()
    missing_info.columns = ['Column', 'Missing_Count']
    missing_info['Missing_Percent'] = (missing_info['Missing_Count'] / len(df)) * 100
    logging.info(f"Missing values details:\n{missing_info}")
    
    #Categorical Feature Insights
    
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        logging.info(f"Top categories in {col}:\n{df[col].value_counts().head(5)}")
    
    #Numerical Feature Insights
    numeric_cols = df.select_dtypes(include=['number']).columns
    logging.info(f"Skewness:\n{df[numeric_cols].skew()}")
    logging.info(f"Kurtosis:\n{df[numeric_cols].kurt()}")
    
    #Outlier Detection (Quick)
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()
        logging.info(f"Outliers in {col}: {outliers}")
        
    #Correlation Check
    logging.info(f"Correlation matrix:\n{df.corr(numeric_only=True)}")
    
    #Sample Data Preview
    
    logging.info(f"First 5 rows:\n{df.head()}")
    logging.info(f"Last 5 rows:\n{df.tail()}")


    





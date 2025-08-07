# Data cleaning and transformation
import logging
import numpy as np

def transform_data(df):
    try:
        print("Check for the missing values......\n")
        print(df.isnull().sum())
        logging.info("Data Cleaning starting with 'Price Column'....")
        df["Price"].isnull().sum() # np.int64(50)
        df["Price"].dtype # dtype('O')
        #Price column contains 'RS' we are trying to remove it
        df["Price"]=df["Price"].str[2:]
        #replace NAN with zero because type of price column is Object 
        df.replace({"Price":{np.nan:0}},inplace=True)
        #convert the object column to integer
        df["Price"]=df["Price"].astype(int)
        #Handling the missing value
        df.replace({"Price":{0:df["Price"].mean()}},inplace=True)
        
        logging.info("Data Cleaning done with Price column....")
        
        logging.info("Data Cleaning Starting with 'Make' column .....")
        
        #missing values
        df["Make"].isnull().sum() #np.int64(49)
        #find the mode of the make column
        df["Make"].value_counts()
        '''
                    Make
            Toyota    379
            Honda     292
            Nissan    183
            BMW        97
            Name: count, dtype: int64
        '''
        #find unique value
        df["Make"].unique() # array(['Nissan', 'Toyota', 'Honda', 'BMW', nan], dtype=object)
        
        #replace missing value with mod
        df.replace({"Make":{np.nan:"Toyota"}},inplace=True)
        
        #again check unique value
        df["Make"].unique()#array(['Nissan', 'Toyota', 'Honda', 'BMW'], dtype=object)
        
        #check the value count
        df["Make"].value_counts()
        '''
                    Make
                Toyota    428
                Honda     292
                Nissan    183
                BMW        97
                Name: count, dtype: int64
        '''
        logging.info("Data Cleaning done with 'Make' column....")
        
        logging.info("Data Cleaning Starting with 'Colour' column....")
        #missing values in colors column
        df["Colour"].isnull().sum() #np.int64(50)
        #find mode
        df["Colour"].value_counts()
        '''
                    Colour
            White    390
            Blue     302
            Black     95
            Red       88
            Green     75
            Name: count, dtype: int64
        '''
        #find unique values
        df["Colour"].unique()# array(['Black', 'White', 'Blue', 'Red', 'Green', nan], dtype=object)
        
        #handle missing values
        df.replace({"Colour":{np.nan:df["Colour"].mode()}},inplace=True)
        
        #check unique values again
        df["Colour"].unique()#array(['Black', 'White', 'Blue', 'Red', 'Green'], dtype=object)
        
        #check the column which contains null values
        df.isnull().sum()
        '''
            Make              0
            Colour            0
            Odometer (KM)    50
            Doors            50
            Price             0
            dtype: int64
        '''
        logging.info("Data Cleaning done with 'Colour' column........")
        
        logging.info("Data Cleaning starting 'Odometer (KM)' column..........")
        
        #checking for missing values
        df["Odometer (KM)"].isnull().sum() #np.int64(50)
        
        #handling missing value
        df["Odometer (KM)"]=df["Odometer (KM)"].fillna(df["Odometer (KM)"].mean())
        
        #checking for missing values
        df["Odometer (KM)"].isnull().sum() #np.int64(0)
        
        logging.info("Data Cleaning done with 'Odometer (KM)' column......")
        
        logging.info("Data Cleaning starting with 'Doors' column.......")
        
        #checking for missing values
        df["Doors"].isnull().sum() #np.int64(50)
        
        #unique values
        df["Doors"].unique() #array([ 4.,  3.,  5., nan])
        
        #value counts
        df["Doors"].value_counts()
        '''
                Doors
            4.0    811
            5.0     75
            3.0     64
            Name: count, dtype: int64
        '''
        #handling the missing value
        df.replace({"Doors":{np.nan:4.0}},inplace=True)
        
        #check null value count
        df["Doors"].isnull().sum() #np.int64(0)
        
        #check unique value count
        df["Doors"].unique() # array([4., 3., 5.])
        
        logging.info("Data Cleaning done with 'Doors' column....")
        
        #cheking for missing value in the dataframe
        print("Missing values in the DataFrame")
        print(df.isnull().sum())
        '''
        Make             0
        Colour           0
        Odometer (KM)    0
        Doors            0
        Price            0
        dtype: int64
        '''
        
        logging.info("Data transformed successfully.")
        return df
    except Exception as e:
        logging.error(f"Error in data transformation: {e}")
        raise

# Optional: model training
import numpy as np  
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
#before apply Label Encoder let's see the unique values
def modeling(df):
    
    df["Make"].value_counts()
    '''
            Make
        Toyota    428
        Honda     292
        Nissan    183
        BMW        97
        Name: count, dtype: int64
    '''
    df["Colour"].value_counts()
    '''
            Colour
        White    440
        Blue     302
        Black     95
        Red       88
        Green     75
        Name: count, dtype: int64
    '''
    #apply label encoder
    lb=LabelEncoder() #creating a object of LabelEncoder
    df["Make"]=lb.fit_transform(df["Make"])
    '''
            Make
        3    428
        1    292
        2    183
        0     97
    '''
    df["Colour"]=lb.fit_transform(df["Colour"])
    '''
        Colour
        4    440
        1    302
        0     95
        3     88
        2     75
    '''
    #findin dependent and independent variable from the dataset
    X=df.drop("Price",axis=1)
    y=df["Price"]
    #split the data into two part 1. training part and testing past
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    logging.info("Data is Successfully Splited into two parts.......")
    print(X_train.shape,y_train.shape,X_test.shape)
    
    #create a object of decision tree regessor
    dt=DecisionTreeRegressor()
    #fit the model
    dt.fit(X_train,y_train)
    logging.info("Model Trained successfully ........")
    
    #prediction
    y_pred=dt.predict(X_test)
    
    logging.info("Model Prediction done.....")
    
    print(y_pred)
    
    logging.info("Modeling Completed Successfully..........")
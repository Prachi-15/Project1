import os                                                        # to make current folder path
import sys                                                       # to handle custom exception in logging
from src.mlproject.exception import CustomException              # to handle custom exception 
from src.mlproject.logger import logging
import pandas as pd
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split

# Input of data ingestion phase:

# 1. data / dataframe from data source that we fetch from sql
# 2. TRAIN DATA PATH
# 3. TEST DATA PATH
# We must give this data path to data ingestion model as an input. 

# Output of data ingestion phase should be train file  and test file that store on particular path.

from dataclasses import dataclass                   # Input parameters are initialized here

@dataclass                                          # @ is define so we can use dataclass 

# dataclass is used to quickly define parameters in any classes.

class DataIngestionConfig:                          
    # It will call __init__() internally by this three variable.      
                  
    train_data_path:str = os.path.join('artifacts', 'train.csv')       # make artifacts folder in which all files are save.
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')           # raw datafile before train test split.

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()   
        
    def initiate_data_ingestion(self):

        try:
            # Step 1: Reading Data from MySQL database in the form of DataFrame.
            # import read_sql_data() function from utils.py
            
            df = read_sql_data()
            logging.info("Reading completed from mysql database")

            # Step 2: Save DataFrame in raw data path.
            # make dir for artifacts: take dir from self.ingestion_config.train_data_path.
            # If folder already exist skip it set exist_ok = True

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)           # To save raw data into that specific path.
                                                                                                   # To not save index but save header.
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)     

            # save train and test set on their particular paths.
            df.to_csv(self.ingestion_config.train_data_path, index = False, header = True) 
            df.to_csv(self.ingestion_config.test_data_path, index = False, header = True) 

            logging.info("Data Ingestion is completed")  

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )     
    
        except Exception as e:
            raise CustomException(e, sys)                                 # e is exception and sys is error parameters.     
        







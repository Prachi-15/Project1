
# Reading data from SQL is created in utils file.
# Util is used for generic fuctionality like import environment variables from .env and reading data from MySQL.

import os                                                        # to make current folder path
import sys                                                       # to handle custom exception in logging
from src.mlproject.exception import CustomException              # to handle custom exception 
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv                                   # to load all environment variables.
import pymysql                                                   # pymysql is responsible for connecting db.


load_dotenv()

host = os.getenv("host")                                   # get environment variable
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL database started.")
    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )

        logging.info("Connection Established", mydb)
        df = pd.read_sql_query('Select * from students',mydb)        # parameters SQL query and db connection into it. # Output dataframe.
        print(df.head())

        return df

    except Exception as ex:
        raise CustomException(ex)

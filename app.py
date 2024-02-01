from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
import sys

# To check logging
# Execution point

if __name__ == "__main__":
    logging.info("The execution has started.")

    try:
        # data_ingestion_config = DataIngestionConfig()            # In data_ingestion DataIngestionConfig() is called inside DataIngestion.  
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)           # Exception capture error message, sys contain remaining info (line no).
    

    

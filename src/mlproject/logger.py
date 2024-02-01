import logging 
import os
from datetime import datetime

# Custom logging: Successful execution and unsuccessful execution caputure in log records.

# log file created in this format with .log extension.

# Setting name of LOG_FILE.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"             

# Path of log folder
# Current working directory of the file we run, "logs is a folder name", "Log is a name of the file"
# getcwd() extract path of the file we ran and make "logs" folder and inside that all LOG_FILE are made.

# Setting path of LOG_FILE.
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)                      

# make folder for log_path
os.makedirs(log_path, exist_ok = True)       # exist_ok = True (if folder already available skip it.)

# Path of complete log file (combine LOG_FILE and log_path)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Their is basicConfig function in logging specify path of LOG_FILE, format
# format (time, lineno : which line no. has problem , name : file name , levelname,
# message : what messsage you need to display for that error.
# we can specify logging.WARNINGS, logging.ERROR

logging.basicConfig(
    filename =  LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,                          
)


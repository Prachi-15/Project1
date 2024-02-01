import sys
from src.mlproject.logger import logging

# taken from python documentation custom exception error detail is of system type.
# error_detail_function give detail about error (file name, line number, ...) whenever their is a exception.

def error_message_detail(error, error_detail:sys):

    # exc_info() brings 3 information.

    _,_,exc_tb = error_detail.exc_info()                 # exc_tb give file information
    file_name = exc_tb.tb_frame.f_code.co_filename       # extract filename from exc_tb, gives file name where exception occur.
    
    error_message =  "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    
    # 0 will replace with file name, 1 will replace with lineno, 2 will replace with error message.

    return error_message


# Make class CustomException which will inherit Exception.
class CustomException(Exception):

    # good to create an initialization constructor
    # sys is used to track error details, assign error_details type as sys.

    def __init__(self, error_message, error_details: sys):
        super.__init__(error_message)            
        
        # error_message_detail takes two paraameters error_message and error_details.

        self.error_message = error_message_detail(error_message, error_details)           

    def __str__(self):
        return self.error_message

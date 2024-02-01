# Write code which will be responsible for creating entire project structure.

# os gives generic folder path
import os

# Path finds relative path of files form the project structure.
from pathlib import Path

# 
import logging

# using basic logging and set basiconfig, want info of logging so set level = logging.INFO

logging.basicConfig(level=logging.INFO)

# we get logging details : provides detail in default format according to time, can also aset this.

# project name

project_name = "mlproject"

# list of files contains all the folder structure

# 1. .github folder structure: 
'''
workflows: contains all the github actions done at the time of deployment
.gitkeep : gives an indication that we are going to  make github folder and we used in deployment.
'''

# 2. src folder structure:
'''
mlproject: contains all the files which are used in the project.
make mlproject a package: create a file __init__.py inside this folder.

ML project mainly contain two things:

1. components folder:    all 6
2. Pipelines:            Training and Prediction Pipelines.
'''

list_of_files = [

    # ".github/workflows/.gitkeep",                                 # workflows folder

    f"src/__init__.py",                                           # Source folder

    f"src/{project_name}/__init__.py",                            # make project folder a package ,used {} so that it become generic.
    f"src/{project_name}/components/__init__.py",                 # components folder make it a package
    f"src/{project_name}/components/data_ingestion.py",           # 1. component: data_ingestion.py
    f"src/{project_name}/components/data_transformation.py",      # 2. data_transformation 
    f"src/{project_name}/components/model_trainer.py",            # 3. model_trainer : data validation is done by config yamal no need to make another file.
    f"src/{project_name}/components/model_monitering.py",         # 4. model_monitering/ evaluation

    f"src/{project_name}/pipelines/__init__.py",                  # pipelines folder: when we compile it it should become a package
    f"src/{project_name}/pipelines/training_pipeline.py",         # 1. training_pipeline
    f"src/{project_name}/pipelines/prediction_pipeline.py",       # 2. prediction_pipeline    

    f"src/{project_name}/exception.py",                           # exception file contain exception handling
    f"src/{project_name}/logger.py",                              # 
    f"src/{project_name}/utils.py",  

    "main.py",                                                    # included after execution of template.py and after executing it again it will only create main.py file and skip already exist file

    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",

]

for filepath in list_of_files:

    filepath = Path(filepath)                             # Path finds relative path from the project
    filedir, filename = os.path.split(filepath)           # on spliting file path we get two things file dir and file name

    # if file dir is not "", then we make directory

    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    # if file path doesnot exist or file is empty the we open it in write mode
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")       # if file already exists ex. requirements.txt in our case.
        






import sys
from typing import Dict, Tuple
import os
import pandas as pd
import pickle # it is used for serializing and deserializing Python object structures.
import yaml # it is used for parsing and writing YAML (YAML Ain't Markup Language) files.
import boto3 # it is the Amazon Web Services (AWS) SDK for Python. sdk stands for software development kit. 

# here we are importing all the constants, exception and logger modules.
# these modules are created by us in this project in src folder using their path.
# which specific functionality we want to use in this module.
from src.constant import *
from src.exception import CustomException
from src.logger import logging




class MainUtils:
    def __init__(self) -> None:
        pass


    def read_yaml_file(self, filename: str) -> dict: # it will read the yaml file and return the content as a dictionary.
        # whenever we want to read any yaml file we can use this fn.
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)


        except Exception as e:
            raise CustomException(e, sys) from e


    def read_schema_config_file(self) -> dict: # it will read the schema.yaml file and return the content as a dictionary.
        # if we want to access the mondo db collections or any other data as schema structure we can use this fn.
        try:
            schema_config = self.read_yaml_file(os.path.join("config", "schema.yaml"))


            return schema_config


        except Exception as e:
            raise CustomException(e, sys) from e


   


    @staticmethod
    def save_object(file_path: str, obj: object) -> None: # this is the indepepndent fn in mainutils class.
        # it will save the object in the file path provided by the user.
        # for example if we want to save the model file or any other object in pickle format we can use this fn.
        logging.info("Entered the save_object method of MainUtils class") # this log will be printed in the log file.
        # because we imported the logging module above


        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj) # here we are using the 'dump()' method of pickle module to serialize the object and write it to the file.
                # we also converted the object into pickle format.


            logging.info("Exited the save_object method of MainUtils class")


        except Exception as e:
            raise CustomException(e, sys) from e


   


    @staticmethod
    def load_object(file_path: str) -> object:
        logging.info("Entered the load_object method of MainUtils class")


        try:
            with open(file_path, "rb") as file_obj:
                obj = pickle.load(file_obj)


            logging.info("Exited the load_object method of MainUtils class")


            return obj


        except Exception as e:
            raise CustomException(e, sys) from e
   
    @staticmethod    # this is duplicate of above load_object fn but without logging.
    def load_object(file_path):
        try:
            with open(file_path,'rb') as file_obj:
                return pickle.load(file_obj)
        except Exception as e:
            logging.info('Exception Occured in load_object function utils')
            raise CustomException(e,sys)
   
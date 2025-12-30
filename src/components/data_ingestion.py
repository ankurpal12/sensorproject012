import sys
import os
import pandas as pd
import numpy as np
from pymongo import MongoClient # this show error so we install pymongo on terminal using pip install pymongo.
from zipfile import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging # we are importing the logging module from logger.py file.
from src.utils.main_utils import MainUtils # we are importing the MainUtils class from main_utils.py file.
from dataclasses import dataclass # it will help to create the class with less code. we don't need to write the __init__ method/constructor.


@dataclass
class DataIngestionConfig:
    artifact_folder: str = os.path.join(artifact_folder) # it will create the artifact folder in the root directory.


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig() # it will create the artifact folder in the root directory.
        self.main_utils = MainUtils() # it will create the object of MainUtils class.

    def export_collection_as_dataframe(self, collection_name: str, db_name):

        try:
            mongo_client = MongoClient(MONGO_DB_URL) # it will create the mongo client object. this url is taken from constant file.

            collection = mongo_client[db_name][collection_name] # it will access the database and collection.

            df = pd.DataFrame(list(collection.find())) # it will convert the collection data into dataframe.

            if "_id" in df.columns.to_list(): # .tolist() will convert the columns into list. if _id column is present in the dataframe then we will drop it.
                df = df.drop(columns=["_id"], axis=1) # axis=1 means we are dropping the column. axis=0 means we are dropping the row.

            df.replace("na", np.nan, inplace=True)

            return df
        except Exception as e:
            raise CustomException(e, sys) from e

    def export_data_into_feature_store_file_path(self)->pd.DataFrame:

        try:
            logging.info("Exporting data from mongodb")
            raw_file_path = self.data_ingestion_config.artifact_folder # this is raw file path where we save the raw data. artifact_folder is the attribute of DataIngestionConfig class which have data_ingestion_config instance.

            os.makedirs(raw_file_path, exist_ok=True) # it will create the raw file path if it does not exist. exist_ok=True means if the folder already exists then it will not raise an error.

            sensor_data = self.export_collection_as_dataframe( # we are calling the export_collection_as_dataframe method and pass the collection name and database name as argument from constant file.
                collection_name = MONGO_COLLECTION_NAME,
                db_name = MONGO_DATABASE_NAME
            )

            logging.info("saving the exported data into feature store file path : {raw_file_path}")

            feature_store_file_path = os.path.join(raw_file_path, "wafer_fault.csv") # it will create the feature store file path where we save the feature store csv file.

            sensor_data.to_csv(feature_store_file_path, index=False) # it will save the dataframe into csv file. index=False is for not to save the index column.

            return feature_store_file_path # it will return the feature store file path.
    
        except Exception as e:
            raise CustomException(e, sys) from e
    
    def initiate_data_ingestion(self) -> Path:

        logging.info(" Entered the initiate_data_ingestion method of dataIngestion class")

        try:
            feature_store_file_path = self.export_data_into_feature_store_file_path() # it will export the data into feature store file path.

            logging.info("got the data from mongodb")

            logging.info("Exited the initiate_data_ingestion method of dataIngestion class")

            return feature_store_file_path
        except Exception as e:
            raise CustomException(e, sys) from e
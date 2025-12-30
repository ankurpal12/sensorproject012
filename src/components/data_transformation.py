import sys
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split    ##############
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass


@dataclass
class DataTransformationConfig:
    artifact_dir = os.path.join("artifacts")
    transfored_train_file_path = os.path.join(artifact_dir, 'train.npy')
    transformed_test_file_path = os.path.join(artifact_dir, 'test.npy')
    trasnformed_object_file_path = os.path.join(artifact_dir,'preprocessor.pkl')
    
class DataTransformation:
    def __init__(self,feature_store_file_path):
        self.feature_store_file_path = feature_store_file_path

        self.data_transformation_config = DataTransformationConfig() # initialize the config dataclass.

        self.utils = MainUtils()

# here we define first method get_data to read the data from the feature store file path.
    @staticmethod
    def get_data(feature_store_file_path: str) -> pd.DataFrame:
        
        try:
            
            data = pd.read_csv(feature_store_file_path)

            data.rename(columns={'Good/Bad': TARGET_COLUMN}, inplace=True) # here target_column is taken from constatn file.

            return data
        except Exception as e:
            raise CustomException(e, sys)

# here next method is get_data_transformer_object which will return the data transformation object.

    def get_data_transformer_object(self):

        try:

            imputer_step = ('imputer', SimpleImputer(strategy='constant', fill_value=0)) # 
            scaler_step = ('scaler', RobustScaler())

            preprocessor = Pipeline(steps=[imputer_step, scaler_step])

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)

            
# here next method is initiate_data_transformation which will initiate the data transformation.

    def initiate_data_transformation(self):

        logging.info("Entered initiate_data_transformation method of Data_Transformation class")

        try:

            dataframe = self.get_data(feature_store_file_path=self.feature_store_file_path)

            X = dataframe.drop(columns=[TARGET_COLUMN], axis=1)
            y = np.where(dataframe[TARGET_COLUMN]==-1,0,1) # converting -1 to 0 and 1 to 1. because we don't want negative values in model training.

        
            X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

            preprocessor = self.get_data_transformer_object()

            X_train_scaled = preprocessor.fit_transform(X_train)
            X_test_scaled = preprocessor.transform(X_test)

            preprocessor_path = self.data_transformation_config.trasnformed_object_file_path
            os.makedirs(os.path.dirname(preprocessor_path), exist_ok=True)


            self.utils.save_object(file_path= preprocessor_path, obj=preprocessor) # we use this from utils file to save the preprocessor object.

            train_arr = np.c_[X_train_scaled, np.array(y_train)] # concatenating the X_train and y_train. n.c_ is used to concatenate the arrays column wise.
            test_arr = np.c_[X_test_scaled, np.array(y_test)] # concatenating the X_test and y_test

            return (train_arr, test_arr, preprocessor_path)
        except Exception as e:
            raise CustomException(e, sys) from e
        






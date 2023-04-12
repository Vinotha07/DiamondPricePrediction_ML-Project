import pandas as pd
import numpy as np
import os
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
from src.components.data_ingestion import DataIngestion







@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path:str=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation: 

    def __init__(self) -> None:
        pass  



    def get_data_transformation_object(self):
        pass




    def initiate_data_transformation:
        pass
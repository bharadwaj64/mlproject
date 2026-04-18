import os 
import sys 

from src.logger import logging 
from src.exception import CustomException

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

from src.exception import CustomException 
from src.logger import logging 

import pickle

def save_object(file_path,obj):
    try:
        logging.info('saving the obj in pickle file')
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,'wb') as file:
            pickle.dump(obj,file)

    except Exception as e:
        raise CustomException(e,sys)

def open_object(file_path):
    try:
        with open(file_path,'rb') as file:
            mp = pickle.load(file)
            return mp 
    except Exception as e:
        raise CustomException(e,sys)
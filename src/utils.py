import os 
import sys 

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

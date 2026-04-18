import os 
import sys 

from src.logger import logging
from src.exception import CustomException

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

from src.utils import open_object

class PredictData:
    def __init__(self):
        pass 

    def predict_data(self,df):
        try:
            scalar_file = 'artifacts/pickle.pkl'
            model_file = 'artifacts/model.pkl'
            preprocessor = open_object(scalar_file)
            regressor = open_object(model_file)

            processed_data = preprocessor.transform(df)
            result = regressor.predict(processed_data)

            return result
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(self,gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def data(self):
        try:
            df = pd.DataFrame({
                'gender': [self.gender],
                'race_ethnicity': [self.race_ethnicity],
                'parental_level_of_education': [self.parental_level_of_education],
                'lunch': [self.lunch],
                'test_preparation_course': [self.test_preparation_course],
                'reading_score': [self.reading_score],
                'writing_score': [self.writing_score]
            })
            result = PredictData().predict_data(df)
            return result 
        except Exception as e:
            raise CustomException(e,sys)



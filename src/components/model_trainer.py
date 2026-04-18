import os 
import sys

from dataclasses import dataclass 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

from src.logger import logging 
from src.exception import CustomException 

from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso 
from sklearn.linear_model import Ridge
from sklearn.svm import SVR 
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.tree import DecisionTreeRegressor 
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor 
from sklearn.ensemble import GradientBoostingRegressor 
from catboost import CatBoostRegressor
from xgboost import XGBRegressor 

from sklearn.model_selection import GridSearchCV

from sklearn.metrics import r2_score

from src.utils import save_object

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info('traing the model has begun')
            X_train,y_train,X_test,y_test = (
            train_arr[:,:-1],
            train_arr[:,-1],
            test_arr[:,:-1],
            test_arr[:,-1]
            )
        
            models: dict = {
                'LinearRegression': LinearRegression(),
                'DecisionTreeRegressor':DecisionTreeRegressor(),
                'RandomForestClassifier':RandomForestRegressor(),
                'AdaBoostRegressor':AdaBoostRegressor(),
                'XGBRegressor':XGBRegressor(),
                'GradientBoostingRegressor':GradientBoostingRegressor(),
                'CatBoostRegressor':CatBoostRegressor(verbose=0)
            }

            params={
                "DecisionTreeRegressor": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                },
                "RandomForestClassifier":{
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                },
                "GradientBoostingRegressor":{
                    'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                },
                "LinearRegression":{
                    'fit_intercept': [True,False]
                },
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                },
                "CatBoostRegressor":{
                    'depth': [6,8,10],
                },
                "AdaBoostRegressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                }
            }

            

            evaluated_models = {}

            for model_name in models.keys():
                regressor = models[model_name]  
                regressor.fit(X_train,y_train)

                predicted_values_test = regressor.predict(X_test)
                test_score = r2_score(y_test,predicted_values_test)

                evaluated_models[model_name] = test_score 

            max_r2_score = 0
            best_model = ''

            for model_name,model_score in evaluated_models.items():
                if model_score > max_r2_score:
                    max_r2_score = model_score
                    best_model = model_name


            gridSearchCV = GridSearchCV(estimator= models[best_model],param_grid= params[best_model],scoring='r2',n_jobs=-1)
            gridSearchCV.fit(X_train,y_train)

            best_predicted_values = gridSearchCV.predict(X_test)
            best_r2_score = r2_score(y_test,best_predicted_values)

            save_object(
                self.model_trainer_config.trained_model_file_path,
                gridSearchCV
            )

            return (
                best_model,best_r2_score
            )

        except Exception as e:
            raise CustomException(e,sys)
        


            






        





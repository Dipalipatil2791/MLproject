## It contains all the code related to reading of data from data source

import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass   # decorator to directly define your class variable
class DataInjestionConfig:
    train_data_path:str =os.path.join('artifacts','train.csv')
    test_data_path:str =os.path.join('artifacts','test.csv')
    row_data_path:str =os.path.join('artifacts','data.csv')
 ## these are inputs given to data injestion compo.,now data injestion compo.
 ## know that where to save these files path.

class DataInjestion:
    def __init__(self):
        self.injestion_config=DataInjestionConfig()
        
    def initiate_data_injestion(self):
        logging.info('Entered the data injestion method or component')
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.injestion_config.train_data_path),exist_ok=True)
         ## getting directory name wrt given path ,exist_ok is for keeping that folder if already their no need to delete it 
        
            df.to_csv(self.injestion_config.row_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.injestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.injestion_config.test_data_path,index=False,header=True)  
            
            logging.info('Injestion of the data is completed')
        
            return (
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path,
                   )
        
        except Exception as e:
            raise CustomException(e,sys)

            
if __name__=='__main__':
     obj=DataInjestion()
     obj.initiate_data_injestion()
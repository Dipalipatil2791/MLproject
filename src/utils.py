### This file contain the functions which we write in comman way and used in entire project


import sys
import os
import dill # another library which helps in creating pickle file


import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging


def save_object(file_path , obj): # using this code we save pickle name in harddisk
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj) # when we dump it ,it will save in filepath

    except Exception as e:
        raise CustomException(e,sys)
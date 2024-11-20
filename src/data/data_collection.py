import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
import yaml
  
#data = pd.read_csv(r"C:\Users\honor\Desktop\water_potability.csv")
def load_data(data_filepath):
    try:
        return pd.read_csv(data_filepath)
    except Exception as e:
        raise Exception(f"Error loading data from {data_filepath}: {e}")

#test_size = yaml.safe_load(open("params.yaml"))["data_collection"]["test_size"]
def load_params(params_filepath): # путь к исходному входном файлу
    try:
        with open(params_filepath, "r") as file: # открываем данный файл в режиме чтения "r"
            params = yaml.safe_load(file)
        return params["data_collection"]["test_size"]
    except Exception as e:
        raise Exception(f"Error loading parameters from {params_filepath}: {e}")


# train_data, test_data = train_test_split(data, test_size=test_size, random_state=42)
def split_data(all_data, test_size):
    try:
        return train_test_split(all_data, test_size=test_size, random_state=42)
    except ValueError as e:
        raise ValueError(f"Error splitting data : {e}")



#data_path = os.path.join("data", "raw")
#os.makedirs(data_path)
#train_data.to_csv(os.path.join(data_path, "train.csv"), index = False)
#test_data.to_csv(os.path.join(data_path, "test.csv"), index = False)
def save_data(df_train_data_or_df_test_data, raw_data_path):
    try:
        df_train_data_or_df_test_data.to_csv(raw_data_path, index = False)
    except Exception as e:
        raise Exception(f"Error saving parameters to {raw_data_path}: {e}")

##############
def main():
    data_filepath = r"C:\Users\honor\Desktop\water_potability.csv"
    params_filepath = "params.yaml"
    raw_data_path = os.path.join("data", "raw") # путь, куда мы помещаем наши обработанные данные после этого этапа (стадии)
    # Внутри этой функции main мы запускаем все наши функции
    try:
        all_data = load_data(data_filepath)
        test_size = load_params(params_filepath) # 0.20
        train_data, test_data = split_data(all_data, test_size)
        os.makedirs(raw_data_path)
        save_data(train_data, os.path.join(raw_data_path, "train.csv"))
        save_data(test_data, os.path.join(raw_data_path, "test.csv"))
    except Exception as e:
        raise Exception(f"An error occurred : {e}")
if __name__ == "__main__":
    main()
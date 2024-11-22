import pandas as pd
import numpy as np
import os

#train_data = pd.read_csv("./data/raw/train.csv") # C:\Users\honor\Desktop\ml_pipeline_papka_na_C_PC\data\raw\train.csv
#test_data = pd.read_csv("./data/raw/test.csv")   # C:\Users\honor\Desktop\ml_pipeline_papka_na_C_PC\data\raw\test.csv
def load_data(raw_data_path):
    try:
        return pd.read_csv(raw_data_path)
    except Exception as e:
        raise Exception(f"Error loading data from {raw_data_path}: {e}")    

#train_processed_data = fill_missing_with_mean(train_data)
#test_processed_data = fill_missing_with_mean(test_data)
def fill_missing_with_median(df_train_data_or_df_test_data):
    try:
        for column in df_train_data_or_df_test_data.columns:
            if df_train_data_or_df_test_data[column].isnull().any():
                median_value = df_train_data_or_df_test_data[column].median() 
                df_train_data_or_df_test_data[column].fillna(median_value,inplace=True) 
        return df_train_data_or_df_test_data
    except Exception as e:
        raise Exception(f"Error Filling missing values : {e}")

#data_path = os.path.join("data","processed")
#os.makedirs(data_path)
#train_processed_data.to_csv(os.path.join(data_path,"train_processed.csv"), index = False)
#test_processed_data.to_csv(os.path.join(data_path,"test_processed.csv"), index = False)
def save_data(df_train_processed_data_or_df_test_processed_data, processed_data_path):
    try:
        df_train_processed_data_or_df_test_processed_data.to_csv(processed_data_path, index = False)
    except Exception as e:
        raise Exception(f"Error saving parameters to {processed_data_path}: {e}")
    

##############
def main():
    raw_data_path = "./data/raw/"
    processed_data_path = "./data/processed"
    try:
        train_data = load_data(os.path.join(raw_data_path, "train.csv"))
        test_data = load_data(os.path.join(raw_data_path, "test.csv"))
        train_processed_data = fill_missing_with_median(train_data)
        test_processed_data = fill_missing_with_median(test_data)
        
        os.makedirs(processed_data_path)
        save_data(train_processed_data, os.path.join(processed_data_path, "train_processed_median.csv"))
        save_data(test_processed_data, os.path.join(processed_data_path, "test_processed_median.csv"))
    except Exception as e:
        raise Exception(f"An error occurred : {e}")
if __name__ == "__main__":
    main()
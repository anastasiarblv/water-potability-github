import numpy as np
import pandas as pd

import pickle
import json

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
#test_data = pd.read_csv("./data/processed/test_processed.csv")
def load_data(test_processed_data_path):
    try:
         return pd.read_csv(test_processed_data_path)
    except Exception as e:
        raise Exception(f"Error loading data from {test_processed_data_path}:{e}")

# Берем то же самое что бы ранее писали в файле model_building.py, но меняем train на test уже
#X_test = test_data.iloc[:,0:-1].values # берем все строки и все столбцы (кроме столбца target, y_test) из test_data
#y_test = test_data.iloc[:,-1].values   # наш целевой (target, y_test) столбец из test_data

def prepare_data(test_processed):
    try:
        X_test = test_processed.drop(columns=['Potability'],axis=1)
        y_test = test_processed['Potability']
        return X_test, y_test
    except Exception as e:
        raise Exception(f"Error Preparing data:{e}")

# Теперь заружаем ранее созданную в файле model_building.py модель, которуя представляет собойт отдельный файл
# model.pkl, который у нас повился после dvc repro на этапе model_building
#model = pickle.load(open("model.pkl", "rb"))
def load_model(model_name_or_model_filepath):
    try:
        with open(model_name_or_model_filepath,"rb") as file:
            model= pickle.load(file)
        return model
    except Exception as e:
        raise Exception(f"Error loading model from {model_name_or_model_filepath}:{e}")

# Теперь сделаем прогнозирование на наших данных X_test
#y_pred = model.predict(X_test)
# И теперь найдем значение показателя Точности (Accuracy Score)
#acc = accuracy_score(y_test, y_pred) # y_test = наши фактические данные, y_pred = наши прогнозные данные, полученные на основе модели
#pre = precision_score(y_test, y_pred)
#recall = recall_score(y_test, y_pred)
#f1score = f1_score(y_test, y_pred)
# Теперь сохраним эти данные (по acc, pre, recall, f1score) в формте JSON,
# для этого создадим словарь metrics_dict
#metrics_dict = {
#    'acc':acc,
#    'precision':pre,
#    'recall' : recall,
#    'f1_score': f1score}

def evaluation_model(model, X_test, y_test):
    try:
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test,y_pred)
        pre = precision_score(y_test,y_pred)
        recall = recall_score(y_test,y_pred)
        f1score = f1_score(y_test,y_pred)

        metrics_dict = {

            'acc':acc,
            'precision':pre,
            'recall' : recall,
            'f1_score': f1score
        }
        return metrics_dict
    except Exception as e:
        raise Exception(f"Error evaluating model : {e}")


# Теперь создадим непосредственно сам файл JSON, и запишем туда наши данные по метрикам:
#with open("metrics.json", "w") as file:
#    json.dump(metrics_dict, file, indent=4)
# Мы создали данный фалй с метриками в формате JSON, чтобы мы могли после всех наших проделанных этапов
# написать в VSCODE команду dvc metrics show, и увидеть значения по всем метрикам для данной модели.
def save_metrics(metrics, metrics_path):
    try:
        with open(metrics_path,'w') as file:
            json.dump(metrics,file,indent=4)
    except Exception as e:
        raise Exception(f"Error saving metrics to {metrics_path}:{e}")
    
##############
def main():
    try:
        test_processed_data_path = "./data/processed/test_processed.csv"
        model_name_or_model_filepath = "models/model.pkl" # тут вместо "model.pkl" пишем уже "models/model.pkl"
        metrics_path = "reports/metrics.json" # тут вместо "metrics.json" пишем уже "reports/metrics.json"

        test_processed = load_data(test_processed_data_path)
        X_test,y_test = prepare_data(test_processed)
        model = load_model(model_name_or_model_filepath)
        metrics = evaluation_model(model,X_test,y_test)
        save_metrics(metrics,metrics_path)
    except Exception as e:
        raise Exception(f"An Error occurred:{e}")

if __name__ == "__main__":
    main()
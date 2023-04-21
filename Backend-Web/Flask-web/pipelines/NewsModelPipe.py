import mlflow as mlf
import os
import tensorflow as tf
import numpy as np


def set_mlflow_env():
    REPO_OWNER = 'h4438'
    USER_TOKEN = '7d5a95fcb968cb2697edf3cc170dcc576e29a6d2'
    os.environ['MLFLOW_TRACKING_USERNAME'] = REPO_OWNER
    os.environ['MLFLOW_TRACKING_PASSWORD'] = USER_TOKEN

def load_mlflow_model(model_path):
    MLFLOW_REPO = "https://dagshub.com/h4438/Stock-Indicator-News.mlflow:5000"
    mlf.set_tracking_uri(MLFLOW_REPO)
    model = mlf.tensorflow.load_model(model_uri=model_path)
    return model

def load_tf_dataset(ds_path):
    return tf.data.Dataset.load(ds_path)

####### infer functions #######

def infer_tf_news(ds_path, model_path):
    set_mlflow_env()
    # tf_ds = load_tf_dataset(ds_path)
    model = load_mlflow_model(model_path)
    # predicts = model.predict(tf_ds)
    # labels = np.argmax(predicts, axis=1)
    # return labels
    print(model)



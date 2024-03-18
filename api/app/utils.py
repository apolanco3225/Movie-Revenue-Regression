import os
import joblib
import numpy as np
import pandas as pd
from io import BytesIO
from pydantic import BaseModel
from sklearn.pipeline import Pipeline
from .schemas import PredictionRequest


def get_model(
    # model_folder = "../models/",
    model_folder="models/",
    model_name="model.pkl",
) -> Pipeline:
    full_model_folder = os.path.join(model_folder, model_name)
    model = joblib.load(full_model_folder)
    return model


def transform_to_array(class_model=BaseModel) -> pd.DataFrame:
    data_dict = {key: [value] for key, value in class_model.dict().items()}
    data_df = pd.DataFrame.from_dict(data_dict)
    data_array = data_df.values
    return data_array


def get_prediction(request: PredictionRequest):
    data = transform_to_array(request)
    model = get_model()
    prediction = model.predict(data)[0]
    return max(0, prediction)

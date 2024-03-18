"""
Additional functionalities for model prediction.
"""

import os
import joblib
import pandas as pd
from pydantic import BaseModel
from sklearn.pipeline import Pipeline


class PredictionRequest(BaseModel):
    """
    Define data schema for API

    """

    production_budget: int
    title_year: int
    aspect_ratio: float
    duration: float
    cast_total_facebook_likes: int
    budget: float
    imdb_score: float
    opening_gross: float
    screens: float

    class Config:
        """Example data schema."""

        json_schema_extra = {
            "example": {
                "production_budget": 425000000,
                "title_year": 2009,
                "aspect_ratio": 1.78,
                "duration": 178.0,
                "cast_total_facebook_likes": 4834,
                "budget": 237000000.0,
                "imdb_score": 7.9,
                "opening_gross": 77025481.0,
                "screens": 3452.0,
            }
        }


class PredictionResponse(BaseModel):
    """
    Create data schema for prediction output.
    """

    worldwide_gross: float


def get_model(
    # model_folder = "../models/",
    model_folder="models/",
    model_name="model.pkl",
) -> Pipeline:
    """
    Load model from memory:
        inputs:
            model_folder: str
            model_name: str
        output:
            model: pickle
    """
    full_model_folder = os.path.join(model_folder, model_name)
    model = joblib.load(full_model_folder)
    return model


def transform_to_array(class_model=BaseModel) -> pd.DataFrame:
    """
    Take json data using the BaseModel schema
    and return data in a numpy array:
    input:
        class_model: json
    output:
        data_array: numpy array
    """
    data_dict = {key: [value] for key, value in class_model.dict().items()}
    data_df = pd.DataFrame.from_dict(data_dict)
    data_array = data_df.values
    return data_array


def get_prediction(request: PredictionRequest):
    """
    Prediction pipeline, from json data to predicted movie value.
    input:
        request: json data
    output:
        prediction: float
    """
    data = transform_to_array(request)
    model = get_model()
    prediction = model.predict(data)[0]
    return max(0, prediction)

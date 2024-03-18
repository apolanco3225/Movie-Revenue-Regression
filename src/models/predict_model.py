import os
import sys
import joblib
import logging
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)

logger.info("Loading model.")
model_folder = "models/"
model_name = "model.pkl"
model_path = os.path.join(model_folder, model_name)
model = joblib.load(model_path)


logger.info("Loading sample data.")
processed_data_folder = "data/processed"
data_path = os.path.join(processed_data_folder, "data.csv")
data = pd.read_csv(data_path)
labels = data.pop("worldwide_gross")
features = data

logger.info("Selecting sample and preprocessing.")
sample = features.iloc[0, :]
sample_array = np.expand_dims(sample.values, axis=0)

logger.info("Model inference")
sample_prediction = model.predict(sample_array)[0]
print(sample_prediction)

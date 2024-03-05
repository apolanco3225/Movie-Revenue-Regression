import os
import sys
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np
from joblib import dump

model_folder = "models/"
model_name = "model.pkl"

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO, 
    datefmt="%H:%M:%S",
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

processed_data_folder = "data/processed"

logger.info("Reading data.")
data_path = os.path.join(processed_data_folder, "data.csv")
data = pd.read_csv(data_path)

labels = data.pop("worldwide_gross")
features = data 

logger.info("Splitting data.")
train_features, test_features, train_labels, test_labels = train_test_split(
    features, 
    labels, 
    test_size=0.2
)


logger.info("Building model.")
model = Pipeline(
    [
        ("imputer", SimpleImputer(missing_values=np.nan, strategy="mean")),
        ("core_model", GradientBoostingRegressor(
            n_estimators=220,
            alpha=0.9,
            ccp_alpha=0.0,
            criterion='friedman_mse',
            init=None,
            learning_rate=0.1,
            loss='squared_error',
            max_depth=3,
            max_features=None,
            max_leaf_nodes=None,
            min_impurity_decrease=0.0,
            min_samples_leaf=1,
            min_weight_fraction_leaf=0.0,
            n_iter_no_change = None, 
            random_state = None,
            subsample=1.0,
            tol=0.0001,
            validation_fraction=0.1,
            verbose=0,
            warm_start=False
        )
        )
    ]
)

logger.info("Training model.")
model.fit(train_features, train_labels)

logger.info("Saving model.")
output_model_folder = os.path.join(model_folder, model_name)
dump(model, output_model_folder)

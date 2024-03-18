import os
import sys
import logging
import pandas as pd


logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)

raw_data_folder = "data/raw"
processed_data_folder = "data/processed"

logger.info("Reading data.")
movies_data_path = os.path.join(raw_data_folder, "movies.csv")
financial_data_path = os.path.join(raw_data_folder, "financials.csv")
opening_data_path = os.path.join(raw_data_folder, "opening_gross.csv")

movies_data = pd.read_csv(movies_data_path)
financial_data = pd.read_csv(financial_data_path)
opening_data = pd.read_csv(opening_data_path)

# merge data
logger.info("Merging data.")
fin_columns = ["movie_title", "production_budget", "worldwide_gross"]
financial_data = financial_data[fin_columns]
data = pd.merge(financial_data, movies_data, on="movie_title", how="left")
data = pd.merge(data, opening_data, on="movie_title", how="left")
data.drop(columns=["movie_title", "gross"], axis=1, inplace=True)
data.dropna(inplace=True)

logger.info("Saving data.")
output_data_dir = os.path.join(processed_data_folder, "data.csv")
data.to_csv(output_data_dir, index=False)

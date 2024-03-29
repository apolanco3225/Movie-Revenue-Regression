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


# current_working_directory = os.getcwd()

# raw_data_folder  = os.path.join(
#     current_working_directory,
#     "../../data/raw"
# )

raw_data_folder = "data/raw"

movies_data_path = os.path.join(raw_data_folder, "movies.csv")
financial_data_path = os.path.join(raw_data_folder, "financials.csv")
opening_data_path = os.path.join(raw_data_folder, "opening_gross.csv")

file_paths = [movies_data_path, financial_data_path, opening_data_path]
trouble_files = []

logging.info("Testing Data Paths.")

for path in file_paths:

    try:
        data = pd.read_csv(path)
    except FileNotFoundError:
        trouble_files.append(path)
        logging.error("An error has occurred while reading %s", path)

    finally:
        logging.info("File located in %s read successfully.", path)


if len(trouble_files) > 0:
    logging.error("The following paths couldn't be read: %s", trouble_files)

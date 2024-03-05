
import pandas as pd
import os


# current_working_directory = os.getcwd()

# raw_data_folder  = os.path.join(
#     current_working_directory, 
#     "../../data/raw"
# )

raw_data_folder  = "data/raw"


movies_data_path  = os.path.join(raw_data_folder, "movies.csv")
financial_data_path = os.path.join(raw_data_folder, "financials.csv")
opening_data_path = os.path.join(raw_data_folder, "opening_gross.csv")

file_paths = [movies_data_path, financial_data_path, opening_data_path]
trouble_files = []

for path in file_paths:

    try:
        data = pd.read_csv(path)
    except:
        trouble_files.append(path)
        raise(f"An error has occurred while reading {path}")
    
    finally:
        print(f"File located in {path} read successfully.")

if len(trouble_files) > 0:
    print(f"The following paths couldn't be read: {trouble_files}")


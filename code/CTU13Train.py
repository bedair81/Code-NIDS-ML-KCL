import pandas as pd
import numpy as np
import pickle
import os, time
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# Reading CSV files, and merging all of them into a single DataFrame
CISIDS2017_folder = "/home/grassfed37/6CCS3PRJ/dummy-ML_NIDS/CICIDS2017ML"
CTU13_folder = "/home/grassfed37/6CCS3PRJ/dummy-ML_NIDS/CTU13ML"

CICIDS2017_df_list = []
CTU13_df_list = []

# Reading CICIDS2017 CSV files into a single DataFrame
for f in os.listdir(CISIDS2017_folder):
    file_path = os.path.join(CISIDS2017_folder, f)
    if os.path.isfile(file_path):
        print("Reading: ", f)
        CICIDS2017_df_list.append(pd.read_csv(file_path))

CICIDS2017_df = pd.concat(CICIDS2017_df_list, ignore_index=True)

# Reading CTU13 CSV files into a single DataFrame
for f in os.listdir(CTU13_folder):
    file_path = os.path.join(CTU13_folder, f)
    if os.path.isfile(file_path):
        print("Reading: ", f)
        CTU13_df_list.append(pd.read_csv(file_path))

CTU13_df = pd.concat(CTU13_df_list, ignore_index=True)


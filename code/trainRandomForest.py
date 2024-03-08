import pandas as pd
import numpy as np
import pickle
import os, time
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


# QUICK PREPROCESSING. 
# Some classifiers do not like "infinite" (inf) or "null" (NaN) values.
CICIDS2017_df.replace([np.inf, -np.inf], np.nan, inplace=True)
print("Columns with problematic values: ", list(CICIDS2017_df.columns[CICIDS2017_df.isna().any()]))
CICIDS2017_df.dropna(inplace=True)

CTU13_df.replace([np.inf, -np.inf], np.nan, inplace=True)
print("Columns with problematic values: ", list(CTU13_df.columns[CTU13_df.isna().any()]))
CTU13_df.dropna(inplace=True)

# Create a new column that unifies all malicious classes into a single class for binary classification
CICIDS2017_df['GT'] = np.where(CICIDS2017_df[' Label']=='BENIGN', 'Benign', 'Malicious')
CTU13_df['GT'] = np.where(CTU13_df[' Label']=='Benign', 'Benign', 'Malicious')

features = pd.Index([
    ' Flow Duration',
    ' Total Fwd Packets',
    ' Total Backward Packets',
    ' Total Length of Bwd Packets',
    ' Fwd Packet Length Max',
    ' Fwd Packet Length Min',
    ' Fwd Packet Length Mean',
    ' Fwd Packet Length Std',
    ' Bwd Packet Length Min',
    ' Bwd Packet Length Mean',
    ' Bwd Packet Length Std',
    ' Flow Packets/s',
    ' Flow IAT Mean',
    ' Flow IAT Std',
    ' Flow IAT Max',
    ' Flow IAT Min',
    ' Fwd IAT Mean',
    ' Fwd IAT Std',
    ' Fwd IAT Max',
    ' Fwd IAT Min',
    ' Bwd IAT Mean',
    ' Bwd IAT Std',
    ' Bwd IAT Max',
    ' Bwd IAT Min',
    ' Bwd PSH Flags',
    ' Fwd Header Length',
    ' Bwd Header Length',
    ' Bwd Packets/s',
    ' Min Packet Length',
    ' Max Packet Length',
    ' Packet Length Mean',
    ' Packet Length Std',
    ' Packet Length Variance',
    ' SYN Flag Count',
    ' RST Flag Count',
    ' ACK Flag Count',
    ' Down/Up Ratio',
    ' Average Packet Size',
    ' Avg Fwd Segment Size',
    ' Avg Bwd Segment Size',
    ' Init_Win_bytes_backward',
    ' act_data_pkt_fwd',
    ' Active Std',
    ' Active Max',
    ' Active Min',
    ' Idle Std',
    ' Idle Max',
    ' Idle Min'
])


# set train variable to the full CTU13 dataset
train = CTU13_df

# set test variable to the full CICIDS2017 dataset
test = CICIDS2017_df

# Train and test a (binary) RandomForestClassifier, printing some basic performance scores, training time, and confusion matrix
start = time.time()
rfClf_bin = RandomForestClassifier(n_jobs = -2)
rfClf_bin.fit(train[features], train['GT'])
end = time.time() - start
print("Training time: ", end)

# Save the binary RandomForestClassifier model
with open('rfClf_bin.pkl', 'wb') as file:
    pickle.dump(rfClf_bin, file)

predictions_bin = rfClf_bin.predict(test[features])
print("Acc: {:3f}".format(accuracy_score(test['GT'], predictions_bin)))
print("F1-score: {:3f}".format(f1_score(test['GT'], predictions_bin, pos_label = 'Malicious')))
pd.crosstab(test['GT'], predictions_bin, rownames=['True'], colnames=['Pred'])

# Train and test a (multiclass) RandomForestClassifier, printing some basic performance scores, training time, and confusion matrix
start = time.time()
rfClf_multi = RandomForestClassifier(n_jobs = -2)
rfClf_multi.fit(train[features], train[' Label'])
end = time.time() - start
print("Training time: ", end)

# Save the multiclass RandomForestClassifier model
with open('rfClf_multi.pkl', 'wb') as file:
    pickle.dump(rfClf_multi, file)
    
predictions_multi = rfClf_multi.predict(test[features])
print("Acc: {:3f}".format(accuracy_score(test[' Label'], predictions_multi)))
print("F1-score: {:3f}".format(f1_score(test[' Label'], predictions_multi, average='macro')))
pd.crosstab(test[' Label'], predictions_multi, rownames=['True'], colnames=['Pred'])

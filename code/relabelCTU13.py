import pandas as pd

# Load the CTU13 dataset
ctu13_df = pd.read_csv('CTU13/CTU13_Attack_Traffic.csv')

# Define column mapping
column_mapping = {
    'Flow Duration': ' Flow Duration',
    'Tot Fwd Pkts': ' Total Fwd Packets',
    'Tot Bwd Pkts': ' Total Backward Packets',
    'TotLen Bwd Pkts': ' Total Length of Bwd Packets',
    'Fwd Pkt Len Max': ' Fwd Packet Length Max',
    'Fwd Pkt Len Min': ' Fwd Packet Length Min',
    'Fwd Pkt Len Mean': ' Fwd Packet Length Mean',
    'Fwd Pkt Len Std': ' Fwd Packet Length Std',
    'Bwd Pkt Len Min': ' Bwd Packet Length Min',
    'Bwd Pkt Len Mean': ' Bwd Packet Length Mean',
    'Bwd Pkt Len Std': ' Bwd Packet Length Std',
    'Flow Pkts/s': ' Flow Packets/s',
    'Flow IAT Mean': ' Flow IAT Mean',
    'Flow IAT Std': ' Flow IAT Std',
    'Flow IAT Max': ' Flow IAT Max',
    'Flow IAT Min': ' Flow IAT Min',
    'Fwd IAT Mean': ' Fwd IAT Mean',
    'Fwd IAT Std': ' Fwd IAT Std',
    'Fwd IAT Max': ' Fwd IAT Max',
    'Fwd IAT Min': ' Fwd IAT Min',
    'Bwd IAT Mean': ' Bwd IAT Mean',
    'Bwd IAT Std': ' Bwd IAT Std',
    'Bwd IAT Max': ' Bwd IAT Max',
    'Bwd IAT Min': ' Bwd IAT Min',
    'Bwd PSH Flags': ' Bwd PSH Flags',
    'Fwd Header Len': ' Fwd Header Length',
    'Bwd Header Len': ' Bwd Header Length',
    'Bwd Pkts/s': ' Bwd Packets/s',
    'Pkt Len Min': ' Min Packet Length',
    'Pkt Len Max': ' Max Packet Length',
    'Pkt Len Mean': ' Packet Length Mean',
    'Pkt Len Std': ' Packet Length Std',
    'Pkt Len Var': ' Packet Length Variance',
    'SYN Flag Cnt': ' SYN Flag Count',
    'RST Flag Cnt': ' RST Flag Count',
    'ACK Flag Cnt': ' ACK Flag Count',
    'Down/Up Ratio': ' Down/Up Ratio',
    'Pkt Size Avg': ' Average Packet Size',
    'Fwd Seg Size Avg': ' Avg Fwd Segment Size',
    'Bwd Seg Size Avg': ' Avg Bwd Segment Size',
    'Init Bwd Win Byts': ' Init_Win_bytes_backward',
    'Fwd Act Data Pkts': ' act_data_pkt_fwd',
    'Active Std': ' Active Std',
    'Active Max': ' Active Max',
    'Active Min': ' Active Min',
    'Idle Std': ' Idle Std',
    'Idle Max': ' Idle Max',
    'Idle Min': ' Idle Min',
    'Label': ' Label'
}

# Rename columns
ctu13_df.rename(columns=column_mapping, inplace=True)

# Change the label of the benign traffic '0' to 'BENIGN'
# Change the label of the attack traffic '1' to 'Botnet'
ctu13_df[' Label'] = ctu13_df[' Label'].replace({0: 'BENIGN', 1: 'Botnet'})

# Define the desired order of columns
cicids2017_columns_order = [
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
    ' Idle Min',
    ' Label'
]

# Reorder the columns in CTU13 DataFrame
ctu13_df = ctu13_df[cicids2017_columns_order]

# Save the relabeled dataset
ctu13_df.to_csv('CTU13ML/CTU13_Attack_Traffic_Relabeled.csv', index=False)
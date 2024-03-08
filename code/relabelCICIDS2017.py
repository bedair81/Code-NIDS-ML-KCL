import pandas as pd

# Load the CTU13 dataset
ctu13_df = pd.read_csv('CTU13/CTU13_Normal_Traffic.csv')

# Load the CICIDS2017 dataset
cicids2017_df = pd.read_csv('CICIDS2017/Wednesday-workingHours.pcap_ISCX.csv')

# Define column mapping for CTU13
column_mapping_ctu13 = {
    'Flow Duration': ' Flow Duration',
    'Tot Fwd Pkts': ' Total Fwd Packets',
    'Tot Bwd Pkts': ' Total Backward Packets',
    'TotLen Fwd Pkts': ' Total Length of Fwd Packets',
    'TotLen Bwd Pkts': ' Total Length of Bwd Packets',
    'Fwd Pkt Len Max': ' Fwd Packet Length Max',
    'Fwd Pkt Len Min': ' Fwd Packet Length Min',
    'Fwd Pkt Len Mean': ' Fwd Packet Length Mean',
    'Fwd Pkt Len Std': ' Fwd Packet Length Std',
    'Bwd Pkt Len Max': ' Bwd Packet Length Max',
    'Bwd Pkt Len Min': ' Bwd Packet Length Min',
    'Bwd Pkt Len Mean': ' Bwd Packet Length Mean',
    'Bwd Pkt Len Std': ' Bwd Packet Length Std',
    'Flow Byts/s': ' Flow Bytes/s',
    'Flow Pkts/s': ' Flow Packets/s',
    'Flow IAT Mean': ' Flow IAT Mean',
    'Flow IAT Std': ' Flow IAT Std',
    'Flow IAT Max': ' Flow IAT Max',
    'Flow IAT Min': ' Flow IAT Min',
    'Fwd IAT Tot': ' Fwd IAT Total',
    'Fwd IAT Mean': ' Fwd IAT Mean',
    'Fwd IAT Std': ' Fwd IAT Std',
    'Fwd IAT Max': ' Fwd IAT Max',
    'Fwd IAT Min': ' Fwd IAT Min',
    'Bwd IAT Tot': ' Bwd IAT Total',
    'Bwd IAT Mean': ' Bwd IAT Mean',
    'Bwd IAT Std': ' Bwd IAT Std',
    'Bwd IAT Max': ' Bwd IAT Max',
    'Bwd IAT Min': ' Bwd IAT Min',
    'Bwd PSH Flags': ' Bwd PSH Flags',
    'Fwd Header Len': ' Fwd Header Length',
    'Bwd Header Len': ' Bwd Header Length',
    'Fwd Pkts/s': ' Fwd Packets/s',
    'Bwd Pkts/s': ' Bwd Packets/s',
    'Pkt Len Min': ' Min Packet Length',
    'Pkt Len Max': ' Max Packet Length',
    'Pkt Len Mean': ' Packet Length Mean',
    'Pkt Len Std': ' Packet Length Std',
    'Pkt Len Var': ' Packet Length Variance',
    'FIN Flag Cnt': ' FIN Flag Count',
    'SYN Flag Cnt': ' SYN Flag Count',
    'RST Flag Cnt': ' RST Flag Count',
    'ACK Flag Cnt': ' ACK Flag Count',
    'Down/Up Ratio': ' Down/Up Ratio',
    'Pkt Size Avg': ' Average Packet Size',
    'Fwd Seg Size Avg': ' Avg Fwd Segment Size',
    'Bwd Seg Size Avg': ' Avg Bwd Segment Size',
    'Init Bwd Win Byts': ' Init_Win_bytes_backward',
    'Fwd Act Data Pkts': ' act_data_pkt_fwd',
    'Active Mean': ' Active Mean',
    'Active Std': ' Active Std',
    'Active Max': ' Active Max',
    'Active Min': ' Active Min',
    'Idle Mean': ' Idle Mean',
    'Idle Std': ' Idle Std',
    'Idle Max': ' Idle Max',
    'Idle Min': ' Idle Min',
    'Label': ' Label'
}

# Rename columns in CTU13 DataFrame
ctu13_df.rename(columns=column_mapping_ctu13, inplace=True)

# Change the label of the benign traffic '0' to 'BENIGN'
# Change the label of the attack traffic '1' to 'Bot'
ctu13_df[' Label'] = ctu13_df[' Label'].replace({0: 'BENIGN', 1: 'Bot'})

# Get the list of columns in CTU13 DataFrame
ctu13_columns = ctu13_df.columns.tolist()

# Get the common columns between CTU13 and CICIDS2017
common_columns = [col for col in ctu13_columns if col in cicids2017_df.columns]

# Reorder and select the common columns in CICIDS2017 DataFrame
cicids2017_df = cicids2017_df[common_columns]

# Save the updated CICIDS2017 dataset
cicids2017_df.to_csv('CICIDS2017ML/Wednesday-workingHours.pcap_ISCX_Relabeled.csv', index=False)
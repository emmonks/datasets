import pandas as pd
import sys

import numpy as np

arquivo=sys.argv[1]

classe=sys.argv[2]

print arquivo
print classe

df = pd.read_csv (arquivo)

#df['Volume']=(df['Total Length of Fwd Packet'] + df['Total Length of Bwd Packet'])
#df['Razao'] = (df['Total Bwd packets'] / df['Total Fwd Packet']) * 100

df['Volume']=(df['Total Length of Fwd Packet'] + df['Total Length of Bwd Packet'])
# Filtro de streaming
df2=df[(df['Volume'] > 8000000)]
df2=df2[(df2['Src IP'] == '2804:04B0:10AA:2500:020C:29FF:FE64:3255') | (df2['Dst IP'] == '2804:04B0:10AA:2500:020C:29FF:FE64:3255')]
df2=df2[(df2['Dst Port'] == 443) & (df2['Protocol'] == 17)]



#df2=df

# Remover campos
if 'Flow ID' in df2.columns:
    del df2['Flow ID']
#del df2["Flow ID"]
if 'Src IP' in df2.columns:
    del df2["Src IP"]
if 'Src Port' in df2.columns:
    del df2["Src Port"]
if 'Dst IP' in df2.columns:
    del df2["Dst IP"]
if 'Dst Port' in df2.columns:
    del df2["Dst Port"]
if 'Protocol' in df2.columns:
    del df2["Protocol"]
if 'Timestamp' in df2.columns:
    del df2["Timestamp"]
if 'Volume' in df2.columns:
    del df2["Volume"]

if 'Fwd Packet Length Max' in df2.columns:
    del df2["Fwd Packet Length Max"]
if 'Fwd Packet Length Min' in df2.columns:
    del df2["Fwd Packet Length Min"]
if 'Bwd Packet Length Max' in df2.columns:
    del df2["Bwd Packet Length Max"]
if 'Bwd Packet Length Min' in df2.columns:
    del df2["Bwd Packet Length Min"]
if 'Flow IAT Max' in df2.columns:
    del df2["Flow IAT Max"]
if 'Flow IAT Min' in df2.columns:
    del df2["Flow IAT Min"]
if 'Fwd IAT Max' in df2.columns:
    del df2["Fwd IAT Max"]
if 'Fwd IAT Min' in df2.columns:
    del df2["Fwd IAT Min"]
if 'Bwd IAT Max' in df2.columns:
    del df2["Bwd IAT Max"]
if 'Bwd IAT Min' in df2.columns:
    del df2["Bwd IAT Min"]
if 'Fwd PSH Flags' in df2.columns:
    del df2["Fwd PSH Flags"]
if 'Bwd PSH Flags' in df2.columns:
    del df2["Bwd PSH Flags"]
if 'Fwd URG Flags' in df2.columns:
    del df2["Fwd URG Flags"]
if 'Bwd URG Flags' in df2.columns:
    del df2["Bwd URG Flags"]
if 'Packet Length Min' in df2.columns:
    del df2["Packet Length Min"]
if 'Packet Length Max' in df2.columns:
    del df2["Packet Length Max"]
if 'FIN Flag Count' in df2.columns:
    del df2["FIN Flag Count"]
if 'SYN Flag Count' in df2.columns:
    del df2["SYN Flag Count"]
if 'RST Flag Count' in df2.columns:
    del df2["RST Flag Count"]
if 'PSH Flag Count' in df2.columns:
    del df2["PSH Flag Count"]
if 'ACK Flag Count' in df2.columns:
    del df2["ACK Flag Count"]
if 'URG Flag Count' in df2.columns:
    del df2["URG Flag Count"]
if 'CWR Flag Count' in df2.columns:
    del df2["CWR Flag Count"]
if 'ECE Flag Count' in df2.columns:
    del df2["ECE Flag Count"]
if 'Fwd Bytes/Bulk Avg' in df2.columns:
    del df2["Fwd Bytes/Bulk Avg"]
if 'Fwd Packet/Bulk Avg' in df2.columns:
    del df2["Fwd Packet/Bulk Avg"]
if 'Fwd Bulk Rate Avg' in df2.columns:
    del df2["Fwd Bulk Rate Avg"]
if 'Subflow Fwd Packets' in df2.columns:
    del df2["Subflow Fwd Packets"]
if 'Subflow Fwd Bytes' in df2.columns:
    del df2["Subflow Fwd Bytes"]
if 'Subflow Bwd Packets' in df2.columns:
    del df2["Subflow Bwd Packets"]
if 'Subflow Bwd Bytes' in df2.columns:
    del df2["Subflow Bwd Bytes"]
if 'FWD Init Win Bytes' in df2.columns:
    del df2["FWD Init Win Bytes"]
if 'Bwd Init Win Bytes' in df2.columns:
    del df2["Bwd Init Win Bytes"]
if 'Fwd Seg Size Min' in df2.columns:
    del df2["Fwd Seg Size Min"]
if 'Active Max' in df2.columns:
    del df2["Active Max"]
if 'Active Min' in df2.columns:
    del df2["Active Min"]
if 'Idle Max' in df2.columns:
    del df2["Idle Max"]
if 'Idle Min' in df2.columns:
    del df2["Idle Min"]


df2=df2.replace('NeedManualLabel', classe)

saida = "dataset_" + classe + ".csv"
df2.to_csv(saida,index=False)



#df2.to_csv('data_cic_28082021_filtroOutros.csv',index=False)


# Total
count1 = df2['Flow Duration'].count()
print('Total de registros: ' + str(count1) + '\n')

#print ('Duracao dos fluxos: \n')
#final_df2 = df2.sort_values(by=['Flow Duration'], ascending=False)
#final_df2 = df2.sort_values(by=['Total Fwd Packet','Flow Duration'], ascending=False)
#print final_df2['Total Fwd Packet'] 
#print final_df2['Flow Duration']

#print df2

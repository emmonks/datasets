import pandas as pd
# Carrega o dataset em CSV
df = pd.read_csv (r'/home/core/flows_iscx2016-2_videos_filtrado_out.csv')


# Seleciona apenas as linhas nas quais a coluna Label = video
df2=df[df['Label'] == "video"]
#df2=df[df['Label'] == "file_transfer"]
#df2=df[df['Label'] == "chat"]
#df2=df[df['Label'] == "spotify"]

# Filtra os registros onde total de pacotes de upload e download sao maiores que 1000
df2=df2[(df2['Total Fwd Packet'] > 1000) & (df2['Total Bwd Packets'] > 100) & (df2['Flow Duration'] > 500000)]

df2.to_csv('data.csv')

# Converte as colunas FWD/BWD IAT Mean de microsegundos para milisegundos
df2['Fwd IAT Mean'] = df2['Fwd IAT Mean'] / 1000
df2['Bwd IAT Mean'] = df2['Bwd IAT Mean'] / 1000


# Razao entre pacotes recebido e enviados
df2['Razao'] = (df2['Total Bwd Packets'] / df2['Total Fwd Packet']) * 100

# Gera estatisticas das colunas desejadas
grouped_single1 = df2.groupby('Label').agg({'Fwd IAT Mean': ['mean', 'min', 'max', 'std']})
grouped_single2 = df2.groupby('Label').agg({'Bwd IAT Mean': ['mean', 'min', 'max', 'std']})
grouped_single3 = df2.groupby('Label').agg({'Fwd Packet Length Mean': ['mean', 'min', 'max', 'std']})
grouped_single4 = df2.groupby('Label').agg({'Bwd Packet Length Mean': ['mean', 'min', 'max', 'std']})
grouped_single5 = df2.groupby('Label').agg({'Total Fwd Packet': ['mean', 'min', 'max', 'std']})
grouped_single6 = df2.groupby('Label').agg({'Total Bwd Packets': ['mean', 'min', 'max', 'std']})
grouped_single7 = df2.groupby('Label').agg({'Average Packet Size': ['mean', 'min', 'max', 'std']})
grouped_single8 = df2.groupby('Label').agg({'Total Length of Fwd Packet': ['mean', 'min', 'max', 'std']})
grouped_single9 = df2.groupby('Label').agg({'Total Length of Bwd Packet': ['mean', 'min', 'max', 'std']})
grouped_single10 = df2.groupby('Label').agg({'Razao': ['mean', 'min', 'max', 'std']})
grouped_single11 = df2.groupby('Label').agg({'Flow Duration': ['mean', 'min', 'max', 'std']})

# Apresenta os resultados dos agrupamentos
print(grouped_single1)
print(grouped_single2)
print(grouped_single3)
print(grouped_single4)
print(grouped_single5)
print(grouped_single6)
print(grouped_single7)
print(grouped_single8)
print(grouped_single9)
print(grouped_single10)
print(grouped_single11)

#print ('Razao entre pacotes de download e upload: ' + str(razao))

# Total
count1 = df2['Label'].count()
print('Total de registros: ' + str(count1) + '\n')

print ('Duracao dos fluxos: \n')
#final_df2 = df2.sort_values(by=['Flow Duration'], ascending=False)
final_df2 = df2.sort_values(by=['Total Fwd Packet','Flow Duration'], ascending=False)
print final_df2['Total Fwd Packet'] 
print final_df2['Flow Duration']

print df2

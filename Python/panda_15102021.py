#!/usr/bin/python

import sys
import pandas as pd

import numpy as np

arquivo=sys.argv[1]

classe=sys.argv[2]

print arquivo
print classe

# Carrega o dataset em CSV
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/Saida/vimeo1.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/Saida/youtube1_25072021.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/Saida/youtube2_25072021.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/Saida/youtube3_25072021.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/Saida/facebook_watch1_25072021.pcap_Flow.csv')

#df = pd.read_csv (r'/home/emmonks/Resultados/29072021/dataset_privado_29072021.csv')

#df = pd.read_csv (r'/home/emmonks/Resultados/31072021/youtube_31072021_35x.pcap_Flow.csv')

#df = pd.read_csv (r'/home/emmonks/Scripts/data_cic_31072021_video_teste.csv')
#df = pd.read_csv (r'/home/emmonks/Resultados/02082021/fixwebcapt_19062021.pcapng.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/02082021/Saida/webcapt_02082021_fix.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/05082021/Saida/webcapt_04082021_E.pcap_Flow.csv')

#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/10082021/Saida/youtube_10082021_take4_filtro.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/12082021/Saida/http_tudo.pcap_Flow.csv')

#df = pd.read_csv (r'/home/emmonks/Resultados/youtube_video1_10m_IE.pcapng.pcap_Flow.csv')

#df = pd.read_csv (r'/home/emmonks/final_flows_iscx2016-2.csv')

#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/13082021/Saida/tudao.txt')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/13082021/Saida/quic.cap_Flow.csv')

#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/12082021/Saida/http_tudo.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/12082021/Saida/dns_tudo.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/12082021/Saida/ftp_all.tcpdump.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/12082021/Saida/ssh_tudo.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/20082021/Saida/quic_20082021.pcap_FlowB.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/21082021/Saida/VM_10x_videos_21082021.pcap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/21082021/Saida/quic_mpls_21082021.cap_Flow.csv')
#df = pd.read_csv (r'/home/emmonks/Capturas_Videos/28082021/video_28082021_filtradook.csv')

#df = pd.read_csv (r'/Resultados/03092021/youtube_31072021_35x/Saida/cic_youtube_31072021_35x.txt')


#df = pd.read_csv (r'/Resultados/03092021/arff_files/matriz/youtube_04092021_final_CIC_ok_label.csv')

#df = pd.read_csv (r'/Resultados/03092021/Saida/CIC_tudao_IPV6_05092021.csv')
#df = pd.read_csv (r'/Resultados/03092021/Saida/CIC_tudao_IPV4_05092021.csv')

#df = pd.read_csv (r'/Resultados/07092021/dataset_dns_07092021.csv')
#df = pd.read_csv (r'/Resultados/07092021/dataset_ftp_07092021.csv')
#df = pd.read_csv (r'/Resultados/07092021/dataset_http_07092021.csv')
#df = pd.read_csv (r'/Resultados/07092021/dataset_ssh_07092021.csv')
#df = pd.read_csv (r'/Resultados/07092021/dataset_video_07092021.csv')
#df = pd.read_csv (r'/Resultados/07092021/dataset_video_IPv6_07092021.csv')


#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/ASIA_porta443.csv')

#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443aa')

# UFPEL
#df = pd.read_csv (r'/Resultados/18092021/UFPEL/Individual/dataset_ufpel_18092021-DNS/Saida/dataset_ufpel_18092021-DNS.csv')
#df = pd.read_csv (r'/Resultados/18092021/UFPEL/Individual/dataset_ufpel_18092021-HTTP/Saida/dataset_ufpel_18092021-HTTP.csv')
#df = pd.read_csv (r'/Resultados/18092021/UFPEL/Individual/dataset_ufpel_18092021-HTTPS/Saida/dataset_ufpel_18092021-HTTPS.csv')
#df = pd.read_csv (r'/Resultados/18092021/UFPEL/Individual/dataset_ufpel_18092021-NTP/Saida/dataset_ufpel_18092021-NTP.csv')
#df = pd.read_csv (r'/Resultados/18092021/UFPEL/Individual/dataset_ufpel_18092021-NTP/Saida/dataset_ufpel_18092021-NTP_B.csv')
#df = pd.read_csv (r'/Resultados/18092021/UFPEL/Individual/dataset_ufpel_18092021-QUIC/Saida/dataset_ufpel_18092021-QUIC.csv')

df = pd.read_csv (arquivo)

#ASIA
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443aa')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ab')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ac')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ad')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ae')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443af')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ag')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ah')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ai')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443aj')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ak')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443al')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443am')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443an')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ao')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ap')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443aq')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ar')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443as')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443at')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443au')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443av')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443aw')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ax')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ay')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443az')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443ba')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bb')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bc')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bd')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443be')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bf')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bg')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bh')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bi')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bj')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bk')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bl')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Abacaxi/Saida/Divide/Parte_ASIA_port443bm')


#df = pd.read_csv (r'/Resultados/18092021/ASIA/Individual/porta110/Saida/ASIA_porta110.csv')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Individual/porta123/Saida/ASIA_porta123.csv')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Individual/porta143/Saida/ASIA_porta143.csv')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Individual/porta161/Saida/ASIA_porta161.csv')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Individual/porta22/Saida/ASIA_porta22.csv')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Individual/porta25/Saida/ASIA_porta25.csv')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Individual/porta443Quic/Saida/ASIA_porta443Quic.csv')
#df = pd.read_csv (r'/Resultados/18092021/ASIA/Individual/porta53/Saida/ASIA_porta53.csv')

# Seleciona apenas as linhas nas quais a coluna Label = video
#df2=df[df['Label'] == "video"]
#df2=df[df['Label'] == "file_transfer"]
#df2=df[df['Label'] == "chat"]
#df2=df[df['Label'] == "spotify"]
#df2=df[df['Label'] == "NeedManualLabel"]


#df2=df[((df['Src IP'] == '2804:04B0:10AA:2500:020C:29FF:FE64:3255') | (df['Src IP'] == '192.168.254.232'))]
#df2=df[(df['Src IP'] != '192.168.254.200') & (df['Dst Port'] == 443) & (df['Flow Duration'] > 20000000)]
#df2=df[(df['Protocol'] == 17) & (df['Flow Duration'] > 20000000)]


df['Volume']=(df['Total Length of Fwd Packet'] + df['Total Length of Bwd Packet'])
# 35
#df2=df[(df['Flow Duration'] > 37000000)]
#df2=df[((df['Dst Port'] == 443) | (df['Dst Port'] == 80))]


#df2=df[(df['Volume'] > 1000000)]
#df2=df[(df['Total Bwd packets'] > 3000)]

#df2=df[(df['Dst IP'] == '2804:04B0:0101:0008:0000:0000:0000:000C')]

#df2=df[df['Label'] == "video"]

# Quic
#df2=df[(df['Dst Port'] == 443) & (df['Protocol'] == 17)]
#df2=df[(df['Dst Port'] == 443) & (df['Protocol'] == 17) & (df['Flow Duration'] > 50000)]
#df2=df[(df['Dst Port'] == 443) & (df['Protocol'] == 17) & (df['Flow Duration'] > 50000) & (df['Volume'] > 5000000)]
#df2=df[(df['Dst Port'] == 443) & (df['Protocol'] == 17) & (df['Flow Duration'] > 120000) & (df['Volume'] > 500000) & (df['Down/Up Ratio'] > 5)]
# SSH
#df2=df[(df['Dst Port'] == 50000) & (df['Protocol'] == 6) & (df['Flow Duration'] > 50000)]
#df2=df[(df['Dst Port'] == 22) & (df['Protocol'] == 6) & (df['Flow Duration'] > 50000)]
# HTTP
#df2=df[(df['Dst Port'] == 80) & (df['Protocol'] == 6) & (df['Flow Duration'] > 500000)]
#df2=df[(df['Dst Port'] == 80) & (df['Protocol'] == 6) & (df['Flow Duration'] > 500000) & (df['Volume'] > 8000000)]
# E-mail
#df2=df[(df['Dst Port'] == 25) & (df['Protocol'] == 6) & (df['Flow Duration'] > 50000)]
# UDP
#df2=df[(df['Protocol'] == 6) & (df['Dst Port'] == 53)]
#df2=df[(df['Protocol'] == 17)]

# HTTPS Download
#df2=df[(df['Dst Port'] == 443) & (df['Protocol'] == 6) & (df['Flow Duration'] > 50000)]

# Pacotes
#df2=df[(df['Total Fwd Packet'] > 5000) & (df['Total Bwd packets'] > 1000) & (df['Flow Duration'] > 50000) & (df['Src IP'] != '192.168.254.233')]
#df2=df[(df['Total Fwd Packet'] > 5000) & (df['Total Bwd packets'] > 1000) & (df['Flow Duration'] > 50000)]
# Video
#df2=df[(df['Flow Duration'] > 12000000) & ((df['Dst Port'] == 443) | (df['Dst Port'] == 80))]
#df2=df[(df['Flow Duration'] > 12000000) & (df['Dst Port'] == 443)]
#df2=df[(df['Flow Duration'] > 118999998)]
#df2=df2[(df2['Volume'] > 50000000)]
#df2=df
#df2=df2[df2['Label'] == "video"]

#df2['Fwd IAT Mean'] = df2['Fwd IAT Mean'] / 1000
#df2['Bwd IAT Mean'] = df2['Bwd IAT Mean'] / 1000


#grouped_single13 = df2.groupby('Flow ID').agg({'Fwd IAT Mean': ['mean', 'min', 'max', 'std']})
#grouped_single14 = df2.groupby('Flow ID').agg({'Bwd IAT Mean': ['mean', 'min', 'max', 'std']})
#print(grouped_single13)
#print(grouped_single14)

#print (df2)
#exit()

df['Razao'] = (df['Total Bwd packets'] / df['Total Fwd Packet']) * 100

#df=df[(df['Flow IAT Mean'] > 50000) & (df['Flow IAT Mean'] < 160000)]
#df2=df[(df['Razao'] > 100)]
#df=df[(df['Total Fwd Packet'] > 200)]

#df2=df[(df['Flow Duration'] > 142000000)]

df2=df
#df2=df[(df['Total Bwd packets'] > 100)]

#grouped_single1b = df2.groupby('Label').agg({'Fwd IAT Mean': ['max']})
#grouped_single2b = df2.groupby('Label').agg({'Bwd IAT Mean': ['max']})




# Filtra os registros onde total de pacotes de upload e download sao maiores que 1000
#df2=df2[(df2['Total Fwd Packet'] > 100) & (df2['Total Bwd packets'] > 200) & (df2['Flow Duration'] > 500) & (df2['Dst Port'] == 443) & (df2['Fwd IAT Mean'] > 10) & (df2['Bwd IAT Mean'] > 10) & (df2['Bwd IAT Mean'] < 150) & (df2['Fwd IAT Mean'] < 150)]
#df2=df2[((df2['Flow Duration'] > 300000000) & (df2['Dst Port'] == 443))]
#df2=df2[(df2['Fwd IAT Mean'] > 1000) & (df2['Bwd IAT Mean'] > 1000) & (df2['Bwd IAT Mean'] < 15000000) & (df2['Fwd IAT Mean'] < 15000000)]


result = df2.groupby('Label').agg({'Fwd IAT Mean': ['max']}).iloc[0]['Fwd IAT Mean']['max']
max_fiat = result / 1000
result = df2.groupby('Label').agg({'Bwd IAT Mean': ['max']}).iloc[0]['Bwd IAT Mean']['max']
max_biat = result / 1000

result = df2.groupby('Label').agg({'Active Mean': ['max']}).iloc[0]['Active Mean']['max']
max_active = result / 1000
result = df2.groupby('Label').agg({'Idle Mean': ['max']}).iloc[0]['Idle Mean']['max']
max_idle = result / 1000


#Fwd_Packet_Length_Mean
result = df2.groupby('Label').agg({'Fwd Packet Length Mean': ['max']}).iloc[0]['Fwd Packet Length Mean']['max']
max_Fwd_Packet_Length_Mean = 1500

#Fwd_Packet_Length_Std
result = df2.groupby('Label').agg({'Fwd Packet Length Std': ['max']}).iloc[0]['Fwd Packet Length Std']['max']
max_Fwd_Packet_Length_Std = 719.83123022


#Flow_IAT_Std
result = df2.groupby('Label').agg({'Flow IAT Std': ['max']}).iloc[0]['Flow IAT Std']['max']
max_Flow_IAT_Std = result

#Fwd_IAT_Std
result = df2.groupby('Label').agg({'Fwd IAT Std': ['max']}).iloc[0]['Fwd IAT Std']['max']
max_Fwd_IAT_Std = result

#Bwd_IAT_Total
result = df2.groupby('Label').agg({'Bwd IAT Total': ['max']}).iloc[0]['Bwd IAT Total']['max']
max_Bwd_IAT_Total = 11997889263

result = df2.groupby('Label').agg({'Packet Length Mean': ['max']}).iloc[0]['Packet Length Mean']['max']
max_Packet_Length_Mean = 1500



#Bwd_IAT_Std
result = df2.groupby('Label').agg({'Bwd IAT Std': ['max']}).iloc[0]['Bwd IAT Std']['max']
max_Bwd_IAT_Std = result

# Bwd Bulk Rate Avg
result = df2.groupby('Label').agg({'Bwd Bulk Rate Avg': ['max']}).iloc[0]['Bwd Bulk Rate Avg']['max']
max_Bwd_Bulk_Rate_Avg = 3625705641




#max_fiat = grouped_single1b.max() / 1000
#max_biat = grouped_single2b.max() / 1000
#print (max_fiat)
#print (max_biat)

#exit()

# Converte as colunas FWD/BWD IAT Mean de microsegundos para milisegundos
df2['Fwd IAT Mean'] = df2['Fwd IAT Mean'] / 1000
df2['Bwd IAT Mean'] = df2['Bwd IAT Mean'] / 1000
df2['Flow IAT Mean'] = df2['Flow IAT Mean'] / 1000
#df2['Fwd IAT Max'] = df2['Fwd IAT Max'] / 1000
#df2['Bwd IAT Max'] = df2['Bwd IAT Max'] / 1000
df2['Active Mean'] = df2['Active Mean'] / 1000
df2['Idle Mean'] = df2['Idle Mean'] / 1000

# Razao entre pacotes recebido e enviados
df2['Razao'] = (df2['Total Bwd packets'] / df2['Total Fwd Packet']) * 100
df2['NormFIAT'] = (df2['Fwd IAT Mean'] / max_fiat) * 10
df2['NormBIAT'] = (df2['Bwd IAT Mean'] / max_biat) * 10
max_razao = df2.groupby('Label').agg({'Razao': ['max']}).iloc[0]['Razao']['max']
df2['NormRazao'] = (df2['Razao'] / max_razao) * 10
df2['NormActive'] = (df2['Active Mean'] / max_active) * 10
df2['NormIdle'] = (df2['Idle Mean'] / max_idle) * 10

# Atributos
df2['NormFwd_Packet_Length_Mean'] = (df2['Fwd Packet Length Mean'] / max_Fwd_Packet_Length_Mean) * 10
# Limita em 10 o max
#df2['NormPacket_Length_Mean'] = np.floor((df2['Packet Length Mean'] / max_Packet_Length_Mean) * 10).clip(0,10)
df2['NormPacket_Length_Mean'] = np.clip(((df2['Packet Length Mean'] / max_Packet_Length_Mean) * 10),0,10)
df2['NormFwd_Packet_Length_Std'] = (df2['Fwd Packet Length Std'] / max_Fwd_Packet_Length_Std) * 10
df2['NormFlow_IAT_Std'] = (df2['Flow IAT Std'] / max_Flow_IAT_Std) * 10
df2['NormFwd_IAT_Std'] = (df2['Fwd IAT Std'] / max_Fwd_IAT_Std) * 10
df2['NormBwd_IAT_Total'] = (df2['Bwd IAT Total'] / max_Bwd_IAT_Total) * 10

df2['NormBwd_IAT_Std'] = (df2['Bwd IAT Std'] / max_Bwd_IAT_Std) * 10

df2['NormBwd_Bulk_Rate_Avg'] = (df2['Bwd Bulk Rate Avg'] / max_Bwd_Bulk_Rate_Avg) * 10

#df2=df2[(df2['Flow ID'] == "192.168.254.242-173.194.24.201-45191-443-17")]

#df2 = df2.drop(df2.columns[0],1)


#Remove colunas
#del df2["Dst Port"]




#df2.to_csv('data_cic_12082021_video.csv',index=False)
#df2.to_csv('data_cic_20082021_35.csv',index=False)
#df2.to_csv('data_cic_20082021_quic.csv',index=False)
#df2.to_csv('dataset_video_15102021.csv',index=False)

#df3 = pd.read_csv (r'/home/emmonks/Scripts/data_cic_31072021_video_tmp.csv')
#df3 = df3.drop(df3.columns[0],1)
#df3.to_csv('data_cic_31072021_video.csv')

#exit()


# Razao entre pacotes recebido e enviados
#df2['Razao'] = (df2['Total Bwd packets'] / df2['Total Fwd Packet']) * 100

# Gera estatisticas das colunas desejadas
grouped_single1 = df2.groupby('Label').agg({'Fwd IAT Mean': ['mean', 'min', 'max', 'std']})
grouped_single2 = df2.groupby('Label').agg({'Bwd IAT Mean': ['mean', 'min', 'max', 'std']})
grouped_single3 = df2.groupby('Label').agg({'Fwd Packet Length Mean': ['mean', 'min', 'max', 'std']})
grouped_single4 = df2.groupby('Label').agg({'Bwd Packet Length Mean': ['mean', 'min', 'max', 'std']})
grouped_single5 = df2.groupby('Label').agg({'Total Fwd Packet': ['mean', 'min', 'max', 'std']})
grouped_single6 = df2.groupby('Label').agg({'Total Bwd packets': ['mean', 'min', 'max', 'std']})
grouped_single7 = df2.groupby('Label').agg({'Average Packet Size': ['mean', 'min', 'max', 'std']})
grouped_single8 = df2.groupby('Label').agg({'Total Length of Fwd Packet': ['mean', 'min', 'max', 'std']})
grouped_single9 = df2.groupby('Label').agg({'Total Length of Bwd Packet': ['mean', 'min', 'max', 'std']})
grouped_single10 = df2.groupby('Label').agg({'Razao': ['mean', 'min', 'max', 'std']})
grouped_single11 = df2.groupby('Label').agg({'Flow Duration': ['mean', 'min', 'max', 'std']})
grouped_single12 = df2.groupby('Label').agg({'Flow IAT Mean': ['mean', 'min', 'max', 'std']})
#grouped_single13 = df2.groupby('Dst Port').agg({'Flow IAT Mean': ['mean', 'min', 'max', 'std']})
grouped_single14 = df2.groupby('Label').agg({'NormFIAT': ['mean', 'min', 'max', 'std']})
grouped_single15 = df2.groupby('Label').agg({'NormBIAT': ['mean', 'min', 'max', 'std']})
grouped_single16 = df2.groupby('Label').agg({'NormRazao': ['mean', 'min', 'max', 'std']})
#grouped_single17 = df2.groupby('Label').agg({'Fwd IAT Max': ['mean', 'min', 'max', 'std']})
#grouped_single18 = df2.groupby('Label').agg({'Bwd IAT Max': ['mean', 'min', 'max', 'std']})
grouped_single19 = df2.groupby('Label').agg({'Volume': ['mean', 'min', 'max', 'std']})
grouped_single20 = df2.groupby('Label').agg({'NormActive': ['mean', 'min', 'max', 'std']})
grouped_single21 = df2.groupby('Label').agg({'NormIdle': ['mean', 'min', 'max', 'std']})
grouped_single22 = df2.groupby('Label').agg({'Active Mean': ['mean', 'min', 'max', 'std']})
grouped_single23 = df2.groupby('Label').agg({'Idle Mean': ['mean', 'min', 'max', 'std']})
grouped_single24 = df2.groupby('Label').agg({'NormFwd_Packet_Length_Mean': ['mean', 'min', 'max', 'std']})
grouped_single25 = df2.groupby('Label').agg({'NormFwd_Packet_Length_Std': ['mean', 'min', 'max', 'std']})
grouped_single26 = df2.groupby('Label').agg({'NormFlow_IAT_Std': ['mean', 'min', 'max', 'std']})
grouped_single27 = df2.groupby('Label').agg({'NormFwd_IAT_Std': ['mean', 'min', 'max', 'std']})
grouped_single28 = df2.groupby('Label').agg({'NormBwd_IAT_Total': ['mean', 'min', 'max', 'std']})
grouped_single29 = df2.groupby('Label').agg({'NormBwd_IAT_Std': ['mean', 'min', 'max', 'std']})
grouped_single30 = df2.groupby('Label').agg({'NormBwd_Bulk_Rate_Avg': ['mean', 'min', 'max', 'std']})
grouped_single31 = df2.groupby('Label').agg({'NormPacket_Length_Mean': ['mean', 'min', 'max', 'std']})


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
print(grouped_single12)
#print(grouped_single13)
print(grouped_single14)
print(grouped_single15)
print(grouped_single16)
#print(grouped_single17)
#print(grouped_single18)
print(grouped_single19)
print(grouped_single20)
print(grouped_single21)
print(grouped_single22)
print(grouped_single23)
print(grouped_single24)
print(grouped_single25)
print(grouped_single26)
print(grouped_single27)
print(grouped_single28)
print(grouped_single29)
print(grouped_single30)
print(grouped_single31)




#Flow Duration,Total Fwd Packet,Total Bwd packets,Total Length of Fwd Packet,Total Length of Bwd Packet,Fwd Packet Length Mean,Fwd Packet Length Std,
#Bwd Packet Length Mean,Bwd Packet Length Std,Flow Bytes/s,Flow Packets/s,Flow IAT Mean,Flow IAT Std,Fwd IAT Total,Fwd IAT Mean,Fwd IAT Std,Bwd IAT Total,Bwd IAT Mean,
#Bwd IAT Std,Fwd Header Length,Bwd Header Length,Fwd Packets/s,Bwd Packets/s,Packet Length Mean,Packet Length Std,Packet Length Variance,
#Down/Up Ratio,Average Packet Size,Fwd Segment Size Avg,Bwd Segment Size Avg,Bwd Bytes/Bulk Avg,
#Bwd Packet/Bulk Avg,Bwd Bulk Rate Avg,Fwd Act Data Pkts,Active Mean,Active Std,
#Idle Mean,Idle Std,Label

#Remove colunas
del df2["Flow Duration"]
del df2["Total Fwd Packet"]
del df2["Total Bwd packets"]
del df2["Total Length of Fwd Packet"]
del df2["Total Length of Bwd Packet"]
del df2["Bwd Packet Length Mean"]
del df2["Bwd Packet Length Std"]
del df2["Flow Bytes/s"]
del df2["Flow IAT Mean"]
del df2["Flow IAT Std"]
del df2["Fwd IAT Total"]
del df2["Fwd IAT Mean"]
del df2["Fwd IAT Std"]
del df2["Bwd IAT Mean"]
del df2["Bwd IAT Std"]
del df2["Fwd Header Length"]
del df2["Bwd Header Length"]
del df2["Fwd Packets/s"]
del df2["Bwd Packets/s"]
#del df2["Packet Length Mean"]
del df2["Packet Length Std"]
del df2["Packet Length Variance"]
del df2["Down/Up Ratio"]
del df2["Average Packet Size"]
del df2["Fwd Segment Size Avg"]
del df2["Bwd Segment Size Avg"]
del df2["Bwd Bytes/Bulk Avg"]
del df2["Bwd Packet/Bulk Avg"]
del df2["Bwd Bulk Rate Avg"]
del df2["Fwd Act Data Pkts"]
del df2["Active Mean"]
del df2["Active Std"]
del df2["Idle Mean"]
del df2["Idle Std"]
del df2["Flow Packets/s"]
#Fwd Packet Length Mean,Fwd Packet Length Std,Bwd IAT Total,Label,
#Volume,Razao,NormFIAT,NormBIAT,NormRazao,NormActive,NormIdle,
#NormFwd_Packet_Length_Mean,NormFwd_Packet_Length_Std,NormFlow_IAT_Std,NormFwd_IAT_Std,NormBwd_IAT_Total,NormBwd_IAT_Std,NormBwd_Bulk_Rate_Avg

del df2["Volume"]
del df2["Razao"]
del df2["NormFIAT"]
del df2["NormBIAT"]
del df2["NormRazao"]
del df2["NormActive"]
del df2["NormIdle"]
del df2["NormFlow_IAT_Std"]
del df2["NormFwd_IAT_Std"]
del df2["NormBwd_IAT_Std"]
del df2["NormBwd_Bulk_Rate_Avg"]



#Flow ID,Src IP,Src Port,Dst IP,Dst Port,Protocol,Timestamp,Fwd Packet Length Max,Fwd Packet Length Min,Fwd Packet Length Mean,Fwd Packet Length Std,
#Bwd Packet Length Max,Bwd Packet Length Min,Flow IAT Max,Flow IAT Min,Fwd IAT Max,Fwd IAT Min,Bwd IAT Total,Bwd IAT Max,Bwd IAT Min,Fwd PSH Flags,
#Bwd PSH Flags,Fwd URG Flags,Bwd URG Flags,Packet Length Min,Packet Length Max,FIN Flag Count,SYN Flag Count,RST Flag Count,PSH Flag Count,ACK Flag Count,
#URG Flag Count,CWR Flag Count,ECE Flag Count,Fwd Bytes/Bulk Avg,Fwd Packet/Bulk Avg,Fwd Bulk Rate Avg,Subflow Fwd Packets,Subflow Fwd Bytes,Subflow Bwd Packets,
#Subflow Bwd Bytes,FWD Init Win Bytes,Bwd Init Win Bytes,Fwd Seg Size Min,Active Max,Active Min,Idle Max,Idle Min,Label,NormFwd_Packet_Length_Mean,NormFwd_Packet_Length_Std
#,NormBwd_IAT_Total


if 'Flow ID' in df2.columns:
    del df2['Flow ID']
#del df2["Flow ID"]
if 'Src IP' in df2.columns:
    del df2["Src IP"]
if 'Src port' in df2.columns:
    del df2["Src Port"]
if 'Dst IP' in df2.columns:
    del df2["Dst IP"]
if 'Dst port' in df2.columns:
    del df2["Dst Port"]
if 'Protocol' in df2.columns:
    del df2["Protocol"]
if 'Timestamp' in df2.columns:
    del df2["Timestamp"]
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

#RST Flag Count,PSH Flag Count,ACK Flag Count,
#URG Flag Count,CWR Flag Count,ECE Flag Count,Fwd Bytes/Bulk Avg,Fwd Packet/Bulk Avg,Fwd Bulk Rate Avg,Subflow Fwd Packets,Subflow Fwd Bytes,Subflow Bwd Packets,
#Subflow Bwd Bytes,FWD Init Win Bytes,Bwd Init Win Bytes,Fwd Seg Size Min,Active Max,Active Min,Idle Max,Idle Min,Label,NormFwd_Packet_Length_Mean,NormFwd_Packet_Length_Std
#,NormBwd_IAT_Total

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



#df2.to_csv('data_cic_12082021_video.csv',index=False)
#df2.to_csv('data_cic_20082021_35.csv',index=False)
#df2.to_csv('data_cic_20082021_quic.csv',index=False)
saida = "dataset_" + classe + ".csv"
#df2.to_csv('dataset_video_15102021.csv',index=False)
df2.to_csv(saida,index=False)



#print ('Razao entre pacotes de download e upload: ' + str(razao))

# Total
#count1 = df2['Flow Duration'].count()
#print('Total de registros: ' + str(count1) + '\n')

#print ('Duracao dos fluxos: \n')
#final_df2 = df2.sort_values(by=['Flow Duration'], ascending=False)
#final_df2 = df2.sort_values(by=['Total Fwd Packet','Flow Duration'], ascending=False)
#print final_df2['Total Fwd Packet'] 
#print final_df2['Flow Duration']

#print df2

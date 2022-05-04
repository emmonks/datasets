import pandas as pd
import sys


categoria=sys.argv[1]

df = pd.read_csv (r'/home/core/Capturas/Capturas_Doutorado/final_flows_iscx2016-2.csv')

df2=df[df['Label'] == categoria ]

#df2=df2[(df2['Total Fwd Packet'] > 1000) & (df2['Total Bwd Packets'] > 1000) & (df2['Average Packet Size'] < 1514)]


df2['Fwd IAT Mean'] = df2['Fwd IAT Mean'] / 1000
df2['Bwd IAT Mean'] = df2['Bwd IAT Mean'] / 1000

grouped_single1 = df2.groupby('Label').agg({'Fwd IAT Mean': ['mean', 'min', 'max', 'std']})
grouped_single2 = df2.groupby('Label').agg({'Bwd IAT Mean': ['mean', 'min', 'max', 'std']})
grouped_single3 = df2.groupby('Label').agg({'Fwd Packet Length Mean': ['mean', 'min', 'max', 'std']})
grouped_single4 = df2.groupby('Label').agg({'Bwd Packet Length Mean': ['mean', 'min', 'max', 'std']})
grouped_single5 = df2.groupby('Label').agg({'Total Fwd Packet': ['mean', 'min', 'max', 'std']})
grouped_single6 = df2.groupby('Label').agg({'Total Bwd Packets': ['mean', 'min', 'max', 'std']})
grouped_single7 = df2.groupby('Label').agg({'Average Packet Size': ['mean', 'min', 'max', 'std']})
grouped_single8 = df2.groupby('Label').agg({'Total Length of Fwd Packet': ['mean', 'min', 'max', 'std']})
grouped_single9 = df2.groupby('Label').agg({'Total Length of Bwd Packet': ['mean', 'min', 'max', 'std']})

print(grouped_single1)
print(grouped_single2)
print(grouped_single3)
print(grouped_single4)
print(grouped_single5)
print(grouped_single6)
print(grouped_single7)
print(grouped_single8)
print(grouped_single9)

max1t = df2['Fwd IAT Mean'].max()
max1 = max1t / 1000
min1t = df2['Fwd IAT Mean'].min()
min1 = min1t / 1000
mean1t = df2['Fwd IAT Mean'].mean() 
mean1 = mean1t / 1000

max2t = df2['Bwd IAT Mean'].max()
max2 = max2t / 1000
min2t = df2['Bwd IAT Mean'].min()
min2 = min2t / 1000
mean2t = df2['Bwd IAT Mean'].mean()
mean2 = mean2t / 1000

fpackets = df2['Total Fwd Packet'].mean()
bpackets = df2['Total Bwd Packets'].mean()
rpackets = (fpackets/bpackets) * 100


print "----------------------------"

print ('Mean Flow FIAT Mean (ms): ' + str(mean1))
print ('Max Flow IAT Mean (ms): ' + str(max1))
print ('Min Flow IAT Mean (ms): ' + str(min1))

print ('Mean Flow BIAT Mean (ms): ' + str(mean2))
print ('Max Flow BIAT Mean (ms): ' + str(max2))
print ('Min Flow BIAT Mean (ms): ' + str(min2))

print ('Relation fpackets/bpackets (%): ' + str(rpackets))

import pandas as pd
#df = pd.read_csv (r'/home/core/Capturas/Capturas_Doutorado/videos_iscx2016V.csv')
df = pd.read_csv (r'/home/core/Capturas/Capturas_Doutorado/final_flows_iscx2016-2.csv')

#print (df)
# block 2 - group by
#groupby_sum1 = df.groupby(['Label']).sum() 
#groupby_count1 = df.groupby(['Label']).count()

#print ('Sum of values, grouped by the Label: ' + str(groupby_sum1))
#print ('Count of values, grouped by the Label: ' + str(groupby_count1))

# block 1 - simple stats
#mean1_t = df['Fwd IAT Mean'].mean()
#mean1 = mean1_t / 1000

#mean2_t = df['Bwd IAT Mean'].mean()
#mean2 = mean2_t / 1000
#if df['Label'].str.contains('video').any():
#   print ("video")    

#video_exists = (df['Label'] == 'video').any() 
#print("'video' exists in the dataframe.".format(num=video_exists)) 

#df2=df[df['Label'].str.contains("video")]
df2=df[df['Label'] == "video"]

#df3=df2.query('"Total Fwd Packet" > "500"')

#df2['Total Fwd Packet'] = df2[df2['Total Fwd Packet'] > 100]['Total Fwd Packet']
# Total Fwd Packet,Total Bwd Packets
df2=df2[(df2['Total Fwd Packet'] > 1000) & (df2['Total Bwd Packets'] > 1000)]


#exit()

df2['Fwd IAT Mean'] = df2['Fwd IAT Mean'] / 1000
df2['Bwd IAT Mean'] = df2['Bwd IAT Mean'] / 1000

# group by Team, get mean, min, and max value of Age for each value of Team.
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

#sum1 = df['Salary'].sum()
#max1 = df['Flow IAT Mean'].max()
#min1 = df['Flow IAT Mean'].min()
#count1 = df['Salary'].count()
#median1 = df['Flow IAT Mean'].median() 
#std1 = df['Flow IAT Mean'].std() 
#var1 = df['Flow IAT Mean'].var() 
#dur1_t = df['Flow Duration'].mean()
#dur1 = dur1_t / 1000 / 1000

# print block 1
#print ('Mean Flow FIAT Mean: ' + str(mean1))
#print ('Mean Flow BIAT Mean: ' + str(mean2))
#print ('Sum of salaries: ' + str(sum1))
#print ('Max Flow IAT Mean: ' + str(max1))
#print ('Min Flow IAT Mean: ' + str(min1))
#print ('Count of salaries: ' + str(count1))
#print ('Median Flow IAT Mean: ' + str(median1))
#print ('Std of Flow IAT Means: ' + str(std1))
#print ('Var of Flow IAT Means: ' + str(var1))
#print ('Duration: ' + str(dur1))

import pandas as pd
df = pd.read_csv (r'/home/core/todos_caps.csv')
#print (df)
# block 2 - group by
#groupby_sum1 = df.groupby(['Label']).sum() 
#groupby_count1 = df.groupby(['Label']).count()

#print ('Sum of values, grouped by the Label: ' + str(groupby_sum1))
#print ('Count of values, grouped by the Label: ' + str(groupby_count1))

#df=df[(df['dstport'] > 40000) & (df['srcip'] == "192.168.254.234") & (df['duration'] > 100000)]
df=df[(df['dstport'] > 40000) & (df['duration'] > 500000)]


# block 1 - simple stats
mean1_t = df['mean_fiat'].mean()
mean1 = mean1_t / 1000

mean2_t = df['mean_biat'].mean()
mean2 = mean2_t / 1000


df['Razao'] = (df['total_fpackets'] / df['total_bpackets']) * 100
#razao = df['Razao'].mean

grouped_ip = df.groupby('dstip').agg({'Razao': ['mean', 'min', 'max', 'std']})


#sum1 = df['Salary'].sum()
max1t = df['mean_fiat'].max()
max1 = max1t / 1000
min1t = df['mean_fiat'].min()
min1 = min1t / 1000
max2t = df['mean_biat'].max()
max2 = max2t / 1000
min2t = df['mean_biat'].min()
min2 = min2t / 1000

#count1 = df['Salary'].count()
#median1 = df['Flow IAT Mean'].median()
#std1 = df['Flow IAT Mean'].std()
#var1 = df['Flow IAT Mean'].var()
dur1_t = df['duration'].mean()
dur1 = dur1_t / 1000 / 1000

# print block 1
print ('Mean Flow FIAT Mean (ms): ' + str(mean1))
print ('Mean Flow FIAT Max (ms): ' + str(max1))
print ('Mean Flow FIAT Min (ms): ' + str(min1))

print ('Mean Flow BIAT Mean (ms): ' + str(mean2))
print ('Mean Flow BIAT Max (ms): ' + str(max2))
print ('Mean Flow BIAT Min (ms): ' + str(min2))

#print ('Razao download/upload (%): ' + str(razao))

print ('Mean Flow Duration (s): ' + str(dur1))

print (grouped_ip)

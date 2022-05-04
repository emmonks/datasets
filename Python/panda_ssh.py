import pandas as pd
df = pd.read_csv (r'/home/core/ssh_teste.txt')
#print (df)
# block 2 - group by
#groupby_sum1 = df.groupby(['Label']).sum() 
#groupby_count1 = df.groupby(['Label']).count()

#print ('Sum of values, grouped by the Label: ' + str(groupby_sum1))
#print ('Count of values, grouped by the Label: ' + str(groupby_count1))

# block 1 - simple stats
mean1_t = df['mean_fiat'].mean()
mean1 = mean1_t / 1000

mean2_t = df['mean_biat'].mean()
mean2 = mean2_t / 1000


#sum1 = df['Salary'].sum()
#max1 = df['Flow IAT Mean'].max()
#min1 = df['Flow IAT Mean'].min()
#count1 = df['Salary'].count()
#median1 = df['Flow IAT Mean'].median()
#std1 = df['Flow IAT Mean'].std()
#var1 = df['Flow IAT Mean'].var()
dur1_t = df['duration'].mean()
dur1 = dur1_t / 1000 / 1000

# print block 1
print ('Mean Flow FIAT Mean (ms): ' + str(mean1))
print ('Mean Flow BIAT Mean (ms): ' + str(mean2))


print ('Mean Flow Duration (s): ' + str(dur1))

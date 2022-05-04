import pandas as pd
df = pd.read_csv (r'Capturas/Capturas_Doutorado/videos_iscx2016V.csv')
#print (df)
# block 2 - group by
#groupby_sum1 = df.groupby(['Label']).sum() 
#groupby_count1 = df.groupby(['Label']).count()

#print ('Sum of values, grouped by the Label: ' + str(groupby_sum1))
#print ('Count of values, grouped by the Label: ' + str(groupby_count1))

# block 1 - simple stats
mean1_t = df['Average Packet Size'].mean()
mean1 = mean1_t

#sum1 = df['Salary'].sum()
max1 = df['Average Packet Size'].max()
min1 = df['Average Packet Size'].min()
#count1 = df['Salary'].count()
median1 = df['Average Packet Size'].median() 
std1 = df['Average Packet Size'].std() 
var1 = df['Average Packet Size'].var() 
dur1_t = df['Flow Duration'].mean()
dur1 = dur1_t / 1000 / 1000

# print block 1
print ('Mean Average Packet Size: ' + str(mean1))
#print ('Sum of salaries: ' + str(sum1))
print ('Max Average Packet Size: ' + str(max1))
print ('Min Average Packet Size: ' + str(min1))
#print ('Count of salaries: ' + str(count1))
print ('Median Average Packet Size: ' + str(median1))
print ('Std of Average Packet Size: ' + str(std1))
print ('Var of Average Packet Size: ' + str(var1))
print ('Duration: ' + str(dur1))

# Flow IAT Mean
mean1_t = df['Flow IAT Mean'].mean()
mean1 = mean1_t / 1000

# print block 1
print ('Mean Flow IAT Mean: ' + str(mean1))


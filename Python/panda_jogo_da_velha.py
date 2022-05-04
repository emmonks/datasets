import pandas as pd
df = pd.read_csv (r'/tmp/CONV/jogo_da_velha.pcapng.pcap.txt')
df2 = pd.read_csv (r'/tmp/CONV/jogo_da_velha.pcap.pcap.txt')
#print (df)
# block 2 - group by
#groupby_sum1 = df.groupby(['Label']).sum() 
#groupby_count1 = df.groupby(['Label']).count()

#print ('Sum of values, grouped by the Label: ' + str(groupby_sum1))
#print ('Count of values, grouped by the Label: ' + str(groupby_count1))

# block 1 - simple stats
meanf1_t = df['mean_fiat'].mean()
meanf1 = meanf1_t / 1000

meanb1_t = df['mean_biat'].mean()
meanb1 = meanb1_t / 1000

dur1_t = df['duration'].mean()
dur1 = dur1_t / 1000 / 1000

meanf2_t = df2['mean_fiat'].mean()
meanf2 = meanf2_t / 1000

meanb2_t = df2['mean_biat'].mean()
meanb2 = meanb2_t / 1000

dur2_t = df2['duration'].mean()
dur2 = dur2_t / 1000 / 1000


# print block 1
print ('======== Sem restricoes ==========')
print ('Mean Flow FIAT Mean (ms): ' + str(meanf1))
print ('Mean Flow BIAT Mean (ms): ' + str(meanb1))
print ('Mean Flow Duration (s): ' + str(dur1))
print ('======== Com restricoes ==========')
print ('Mean Flow FIAT Mean (ms): ' + str(meanf2))
print ('Mean Flow BIAT Mean (ms): ' + str(meanb2))
print ('Mean Flow Duration (s): ' + str(dur2))


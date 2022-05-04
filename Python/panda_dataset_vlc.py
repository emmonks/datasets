import pandas as pd
df = pd.read_csv (r'/tmp/CONV/vlc_udp_04072021.pcapng.pcap.txt')
#df2 = pd.read_csv (r'/tmp/CONV/globo_vod_04072021.pcapng.pcap.txt')

#df=df[(df['dstport'] > 40000) & (df['srcip'] == "192.168.254.234") & (df['duration'] > 100000)]
#df=df[(df['dstport'] == 443 ) & (df['total_bpackets'] > 2000)]
#df2=df2[(df2['dstport'] == 443 ) & (df2['total_bpackets'] > 2000)]


# First DF
mean1_t = df['mean_fiat'].mean()
mean1 = mean1_t / 1000

mean2_t = df['mean_biat'].mean()
mean2 = mean2_t / 1000


max1t = df['mean_fiat'].max()
max1 = max1t / 1000
min1t = df['mean_fiat'].min()
min1 = min1t / 1000
max2t = df['mean_biat'].max()
max2 = max2t / 1000
min2t = df['mean_biat'].min()
min2 = min2t / 1000

std1t = df['mean_fiat'].std()
std1 = std1t / 1000

dur1_t = df['duration'].mean()
dur1 = dur1_t / 1000 / 1000


mean1_t = df['mean_fiat'].mean()
mean1 = mean1_t / 1000

mean2_t = df['mean_biat'].mean()
mean2 = mean2_t / 1000

# Second DF

#max1t2 = df2['mean_fiat'].max()
#max12 = max1t2 / 1000
#min1t2 = df2['mean_fiat'].min()
#min12 = min1t2 / 1000
#max2t2 = df2['mean_biat'].max()
#max22 = max2t2 / 1000
#min2t2 = df2['mean_biat'].min()
#min22 = min2t2 / 1000

#std1t2 = df2['mean_fiat'].std()
#std12 = std1t2 / 1000

#dur1_t2 = df2['duration'].mean()
#dur12 = dur1_t2 / 1000 / 1000

#mean1_t2 = df2['mean_fiat'].mean()
#mean12 = mean1_t2 / 1000

#mean2_t2 = df2['mean_biat'].mean()
#mean22 = mean2_t2 / 1000



print "----------------------------"
print "Dataset privado - VLC (VoD)"
print "----------------------------"

print ('Mean Mean Flow FIAT (ms): ' + str(mean1))
print ('Max Mean Flow FIAT (ms): ' + str(max1))
print ('Min Mean Flow FIAT (ms): ' + str(min1))
print ('Std Mean Flow FIAT (ms): ' + str(std1))


print ('Mean Mean Flow BIAT  (ms): ' + str(mean2))
print ('Max Mean Flow BIAT  (ms): ' + str(max2))
print ('Min Mean Flow BIAT  (ms): ' + str(min2))


print ('Mean Flow Duration (s): ' + str(dur1))

#print "----------------------------"
#print "Dataset privado - Globo (VoD)"
#print "----------------------------"

#print ('Mean Mean Flow FIAT (ms): ' + str(mean12))
#print ('Max Mean Flow FIAT (ms): ' + str(max12))
#print ('Min Mean Flow FIAT (ms): ' + str(min12))
#print ('Std Mean Flow FIAT (ms): ' + str(std12))


#print ('Mean Mean Flow BIAT  (ms): ' + str(mean22))
#print ('Max Mean Flow BIAT  (ms): ' + str(max22))
#print ('Min Mean Flow BIAT  (ms): ' + str(min22))


#print ('Mean Flow Duration (s): ' + str(dur12))


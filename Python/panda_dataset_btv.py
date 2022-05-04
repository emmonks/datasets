import pandas as pd
df = pd.read_csv (r'/tmp/CONV/webcapt_19062021_live2_conv.pcap.pcap.txt')

#df=df[(df['dstport'] > 40000) & (df['srcip'] == "192.168.254.234") & (df['duration'] > 100000)]
df=df[(df['dstport'] > 40000) & (df['srcip'] == "192.168.254.234")]


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

print "----------------------------"
print "Dataset privado - BTV"
print "----------------------------"

print ('Mean Mean Flow FIAT (ms): ' + str(mean1))
print ('Max Mean Flow FIAT (ms): ' + str(max1))
print ('Min Mean Flow FIAT (ms): ' + str(min1))
print ('Std Mean Flow FIAT (ms): ' + str(std1))


print ('Mean Mean Flow BIAT  (ms): ' + str(mean2))
print ('Max Mean Flow BIAT  (ms): ' + str(max2))
print ('Min Mean Flow BIAT  (ms): ' + str(min2))


print ('Mean Flow Duration (s): ' + str(dur1))

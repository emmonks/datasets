file=open("campos_fora.txt","r")
#Repeat for each song in the text file
for line in file:
  
  linha = line.split(";")
  campo = linha[0]

  #if 'Fwd Packet Length Max' in df2.columns:
#    del df2["Dst Port"]

  print "if \'",
  print campo + ","
  print "\' in df2.columns:\n"
  print "   del df2[\"", 
  print campo + "\"] \n"
file.close()

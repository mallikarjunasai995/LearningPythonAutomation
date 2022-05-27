NUM_OF_LINES=40000
filename = 'NVM_RW_DataCmp_Q_Err.log'
with open(filename) as fin:
    fout = open("output0.txt","wb")
    for i,line in enumerate(fin):
      fout.write(line)
      if (i+1)%NUM_OF_LINES == 0:
        fout.close()
        fout = open("output%d.txt"%(i/NUM_OF_LINES+1),"wb")

    fout.close()
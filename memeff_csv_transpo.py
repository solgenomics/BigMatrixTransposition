import csv
import sys
import time
time1=time.time()
#One file for read and create a new file for write
readFile=open(sys.argv[1])
writeFile=open(sys.argv[1].replace('.csv','transpose.csv'),"w+")
#determine the dimension of our matrix
with open(sys.argv[1]) as f:
    reader = csv.reader(f, delimiter=',')
    first_row = next(reader)
    num_cols = len(first_row)
num_lines = sum(1 for line in readFile)
print "Initial matrix dimension: ("+str(num_lines)+","+str(num_cols)+")"
#determine the length of all the characters before the begin of the i line
CumulineLength=[0]
with open(sys.argv[1]) as f:
	for line in f:
		CumulineLength+=[CumulineLength[-1]+len(line)]
print("Length calculated")
#We keep an offset eachtime we iterate depending of the amount of data we took
readOffset=[0 for i in range(num_lines)]
#Function that determine how much characters our data take 
def determineChunk(i):
	readFile.seek(CumulineLength[i]+readOffset[i])
	chunk=1
	ch=readFile.read(1)
	while ch!=',' and ch!='\n' and ch!='':
		ch=readFile.read(1)
		chunk+=1
	return chunk
# we iterate verticaly so we can write our file transposed
for j in range(num_cols):
	for i in range(num_lines-1):
		chunk=determineChunk(i)
		#We move the 
		readFile.seek(CumulineLength[i]+readOffset[i])
		writeFile.write(readFile.read(chunk-1)+',')
		readOffset[i]+=chunk
	chunk=determineChunk(num_lines-1)
	readFile.seek(CumulineLength[num_lines-1]+readOffset[num_lines-1])
	writeFile.write(readFile.read(chunk-1)+'\n')
	readOffset[num_lines-1]+=chunk
readFile.close()
writeFile.close()
print'Execution Time:'+str(time.time()-time1)
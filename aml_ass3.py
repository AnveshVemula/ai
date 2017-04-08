import random
import math
f=open("/home/acreddy/Desktop/Occupancy-detection-data-master/datatraining.txt","r")
#print f.read()
lst=[]
for line in f:
	k=[]
	line=line.split(',')
	k.append( float(line[2]))
	k.append(float(line[3]))
	k.append(float(line[4]))
	k.append(float(line[5]))
	k.append(int(line[7]))
	lst.append(k)
random.shuffle(lst)
length = len(lst)
error1=[]
error2=[]
error3=[]


trainingdata=[]
testdata=[]
for i in range(length/3,length):
	trainingdata.append(lst[i])
for i in range(0,length/3):
	testdata.append(lst[i])
for k in range(1,11):
	error=0
	for i in testdata:
		a=sorted(trainingdata,key=lambda x:pow(x[0]-i[0],2)+pow(x[1]-i[1],2)+pow(x[2]-i[2],2)+pow(x[3]-i[3],2))
		count0=0
		count1=0
		for j in range(k):
			if a[j][4]==0:
				count0+=1
			else:
				count1+=1 
		if count0<count1:
			if i[4]==0:
				error+=1
		else:
			if i[4]==1:
				error+=1
	error1.append(float(float(error)/float(len(testdata))))
print error1


trainingdata=[]
testdata=[]
for i in range(0,length/3):
	trainingdata.append(lst[i])
for i in range(2*length/3,length):
	trainingdata.append(lst[i])
for i in range(length/3,2*length/3):
	testdata.append(lst[i])
for k in range(1,11):
	error=0
	for i in testdata:
		a=sorted(trainingdata,key=lambda x:pow(x[0]-i[0],2)+pow(x[1]-i[1],2)+pow(x[2]-i[2],2)+pow(x[3]-i[3],2))
		count0=0
		count1=0
		for j in range(k):
			if a[j][4]==0:
				count0+=1
			else:
				count1+=1 
		if count0<count1:
			if i[4]==0:
				error+=1
		else:
			if i[4]==1:
				error+=1
	error2.append(float(float(error)/float(len(testdata))))
print error2

trainingdata=[]
testdata=[]
for i in range(0,2*length/3):
	trainingdata.append(lst[i])
for i in range(2*length/3,length):
	testdata.append(lst[i])
for k in range(1,11):
	error=0
	for i in testdata:
		a=sorted(trainingdata,key=lambda x:pow(x[0]-i[0],2)+pow(x[1]-i[1],2)+pow(x[2]-i[2],2)+pow(x[3]-i[3],2))
		count0=0
		count1=0
		for j in range(k):
			if a[j][4]==0:
				count0+=1
			else:
				count1+=1 
		if count0<count1:
			if i[4]==0:
				error+=1
		else:
			if i[4]==1:
				error+=1
	error3.append(float(float(error)/float(len(testdata))))
print error3

finalerror=[]
for i in range(10):
	finalerror.append((error1[i]+error2[i]+error3[i])/3)
print "selected k is"+str(min(finalerror))
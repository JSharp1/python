import numpy as np
import time

PATH = 'data2/data.npz.npy'
a = np.load(PATH, 'r',)#load pickled data
print len(a)#print largest dimension
x = a.shape#print dimensions
print x

for i in range(len(a)): #print all cols for each row
	print a[i,:]
	time.sleep(.5)


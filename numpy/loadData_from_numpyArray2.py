import numpy as np
import cv2
import time

PATH = 'data2/data.npz.npy'
a = np.load(PATH, 'r',)
x = a.shape
print x[0]
print len(a)

for i in range(len(a)):
	print a[i,:]
	cv2.imshow("",img)
	# wait for a keyinput
	cv2.waitKey(500) & 0xFF
	# destroy window/s
	cv2.destroyAllWindows()


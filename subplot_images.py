"""
	subplot images loaded with opencv using matplotlib 
	https://matplotlib.org/users/pyplot_tutorial.html#working-with-multiple-figures-and-axes
  
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

PATH = "00000_00000.ppm"

def main():
	# import image as BGR then convert to RGB
	src = cv2.imread(PATH)
	src = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
	cv2.imshow("src", src)
	# create a figure
	plt.figure("fig 1")
	# subplot(nrows,ncols,fignum)
	plt.subplot(2,2,4).imshow(src)
	# remove axis from fig 4
	plt.subplot(2,2,4).axes.get_xaxis().set_visible(False)
	plt.subplot(2,2,4).axes.get_yaxis().set_visible(False)
	plt.subplot(2,2,1).set_title('Axis [0,0]')
	# show
	plt.show()
	cv2.waitKey(0); 
	cv2.destroyAllWindows()
	plt.close('all')

if __name__ == '__main__':
	main()

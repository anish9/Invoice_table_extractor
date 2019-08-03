import cv2
import numpy as np
import os

"""SIMPLE FUNCTION TO EXTRACT PRIMARY TABLES IN INVOICES"""
"""DEFAULT PARAMS SET"""

class Table(object):
	def __init__(self,image_id,output_dir="OUT_DIR"):
		self.image_file = image_id
		self.out_dir = output_dir
		
	def EXTRACT_TABLE(self):
		"""extracts tables with the help of contours utilizing the logic of 
			sizes ininvoices or research files"""
		MAX_AREA = 4
		MIN_HEIGHT = 10
		id_file = self.image_file
		image  = cv2.imread(id_file,0)
		raw = cv2.imread(id_file)
		ret,thr = cv2.threshold(image,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		contour,hier = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		cnts = sorted(contour, key = cv2.contourArea, reverse = True)[1:MAX_AREA]
		xmin = []
		ymin = []
		xmax = []
		ymax = []
		for c in cnts:
			x, y, w, h = cv2.boundingRect(c)
			if h >= MIN_HEIGHT:
				xmin.append(x)
				ymin.append(y)
				xmax.append(x+w)
				ymax.append(y+h)

		for (j),(z,y,x,w) in enumerate(zip(xmin,ymin,xmax,ymax)):
			draws = raw[y:w,z:x]
			cv2.imwrite(self.out_dir+"/"+str(j)+".jpg",draws)
			
	def remove_redun(self):
	
		"""removes noise files in extraction based
		 on image dimension"""

		MIN_HEIGHT,MIN_WIDTH = 50,50
		called_dir = self.out_dir
		for files in os.listdir(called_dir):
			file = os.path.join(called_dir,files)
			im = cv2.imread(file,0)
			height,width = im.shape[0],im.shape[1]
			if height <= MIN_HEIGHT or width <= MIN_WIDTH:
				print(f"removed : {files}")
				os.remove(file)
import cv2
import os

def creat():
	for file_type in ['n']:
	    for img in os.listdir(file_type):
			if file_type == 'n':
				line = file_type+'/'+img+'\n'
				with open('bg.txt', 'a') as f:
					f.write(line)
			elif file_type == 'p':
				line = file_type+'/'+img+' 1 0 0 50 50\n'
				with open('info.dat', 'a') as f:
					f.write(line)

creat()
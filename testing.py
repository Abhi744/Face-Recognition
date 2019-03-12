import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import matplotlib.pyplot as plt
import os
options = {
   'model': 'cfg/tiny-yolo-voc-2c.cfg',
   'load': 4000,
   'threshold': 0.1
}
FOLDER_NAME = 'testing'
allImages = os.listdir(FOLDER_NAME)
tfnet = TFNet(options)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for image in allImages:
	try:
		img = cv2.imread(FOLDER_NAME+'/' +image)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		name = image.split('.')[0]
		resultFile = open(FOLDER_NAME+'/'+ name+'_result.txt','w')
		

		results = tfnet.return_predict(img)
		for i in range(len(results)):
			tl = (results[i]['topleft']['x'], results[i]['topleft']['y'])
			br = (results[i]['bottomright']['x'], results[i]['bottomright']['y'])
			label = results[i]['label']
			if(len(faces) == 0):
				cv2.rectangle(img,tl,br,(255,0,0),2)
		   	
		kejriwal = 0
		modi = 0
		for i in results:
			if(i['label'] == 'Arvind Kejriwal'):
				kejriwal = 1
			if(i['label'] == 'Narendra Modi'):
				modi = 1

		if(kejriwal == 1):
			print('Arvind Kejriwal Present: Yes')
			resultFile.write('Arvind Kejriwal Present: Yes\n')
		else:
			print('Arvind Kejriwal Present: No')
			resultFile.write('Arvind Kejriwal Present: No\n')

		if(modi == 1):
			print('Narendra Modi Present: Yes')
			resultFile.write('Narendra Modi Present: Yes\n')
		else:
			resultFile.write('Narendra Modi Present: No\n')
			print('Narendra Modi Present: No')
		
		if(len(faces) > 0 or modi == 1 or kejriwal == 1):
			print('Face Present: Yes')
			resultFile.write('Face Present: Yes\n')
		else:
			print('Face Present: No')
			resultFile.write('Face Present: No\n')
		resultFile.close()

		for (x,y,w,h) in faces:
		    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

		cv2.imwrite(FOLDER_NAME+ '/'+ name+'_result.jpg',img)
	except:
		print('Could not process this image')

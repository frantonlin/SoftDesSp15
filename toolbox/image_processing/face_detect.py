""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((25,25),'uint8')

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)

		# Left eye
		cv2.circle(frame,(int(x+w*0.31),int(y+h*0.39)),int(w*0.09),(255,255,255),-1)
		cv2.circle(frame,(int(x+w*0.32),int(y+h*0.37)),int(w*0.045),(0,0,0),-1)

		# Right eye
		cv2.circle(frame,(int(x+w-w*0.31),int(y+h*0.39)),int(w*0.09),(255,255,255),-1)
		cv2.circle(frame,(int(x+w-w*0.29),int(y+h*0.40)),int(w*0.045),(0,0,0),-1)

		# Mouth
		cv2.ellipse(frame,(int(x+w*0.5),int(y+h*0.75)),(int(w*0.25),int(h*0.14)),0,20,160,(0,0,0),int(w*0.04))

		#cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))

	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
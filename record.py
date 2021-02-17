import numpy as np
import time
import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors,minSize=(55, 55))
        coords=[]
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
                cv2.putText(img,"Amount : "+str(features.shape[0]),(0,25),cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),1)
                coords=[x,y,w,h]
                coords=[x,y,w,h]
        return img,coords 
        
def detect(img,faceCascade):
        img,coords=draw_boundary(img,faceCascade,1.1,10,(0,255,0),"Face")
        return img

filename = time.strftime("%Y%m%d-%H%M%S")

cap = cv2.VideoCapture(2)

fourcc=cv2.VideoWriter_fourcc(*'MPEG')
out=cv2.VideoWriter(filename+'.avi',fourcc,20.0,(640,480))

while (cap.isOpened()):
        ret,frame = cap.read()
        frame=detect(frame,faceCascade)
        if(ret==True):
            out.write(frame)
            cv2.imshow('frame',frame)
            if(cv2.waitKey(1) & 0xFF== ord('q')):
                break
        else:
            break
        
cap.release()
cv2.destroyAllWindows()

import numpy as np
import cv2


frame = cv2.imread('test.png')

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_rose = np.array([120,100,100])
upper_rose = np.array([160,240,255])
    
lower_yellow = np.array([0,150,100])
upper_yellow = np.array([50,255,200])


lower_blue = np.array([100,60,50])
upper_blue = np.array([130,255,255])



rose = cv2.inRange(hsv, lower_rose, upper_rose)
yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
blue = cv2.inRange(hsv, lower_blue, upper_blue)



kernal = np.ones((5,5),np.uint8)



rose=cv2.dilate(rose, kernal)
res1 = cv2.bitwise_and(frame,frame, mask= rose)


yellow=cv2.dilate(yellow, kernal)
res2 = cv2.bitwise_and(frame,frame, mask= yellow)



blue=cv2.dilate(blue, kernal)
res3 = cv2.bitwise_and(frame,frame, mask= blue)








(_,contours,hierarchy)=cv2.findContours(rose,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):

    area = cv2.contourArea(contour)
    if(area>10000):
        x,y,w,h = cv2.boundingRect(contour) 
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(222,25,255),2)
        cv2.putText(frame,"rose",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (222,25,255))        
        print("rose")



(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):

    area = cv2.contourArea(contour)
    if(area>10000):
        x,y,w,h = cv2.boundingRect(contour) 
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,204,204),2)
        cv2.putText(frame,"yellow",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,204,204))        
        print("yellow")



(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):

    area = cv2.contourArea(contour)
    if(area>10000):
        x,y,w,h = cv2.boundingRect(contour) 
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(2255,0,0),2)
        cv2.putText(frame,"blue",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,0,0))        
        print("blue")





 
    cv2.imshow("Color",frame)


k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()


import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while(cap.isOpened()):

    ret,frame = cap.read()

# frame = cv2.imread('w2.jpg')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# # upper mask (170-180)
# lower_red = np.array([170,50,50])
# upper_red = np.array([180,255,255])


# lower_blue = np.array([105,100,50])
# upper_blue = np.array([140,255,255])

# lower_orenge = np.array([0,200,255])

# upper_orenge = np.array([30,255,255])


    lower_white = np.array([50,100,100])
    upper_white = np.array([70,100,100])
 


# lower_green = np.array([15,150,200])
# upper_green = np.array([75,255,220])





# lower_black = np.array([0,0,0])
# upper_black = np.array([255,10,10])



# red = cv2.inRange(hsv, lower_red, upper_red)
# blue = cv2.inRange(hsv, lower_blue, upper_blue)
# orenge = cv2.inRange(hsv, lower_orenge, upper_orenge)
# green = cv2.inRange(hsv, lower_green, upper_green)
    white = cv2.inRange(hsv, lower_white, upper_white)
# black= cv2.inRange(hsv, lower_black, upper_black)


    kernal = np.ones((5,5),np.uint8)



# red=cv2.dilate(red, kernal)
# res1 = cv2.bitwise_and(frame,frame, mask= red)


# blue=cv2.dilate(blue, kernal)
# res2 = cv2.bitwise_and(frame,frame, mask= blue)



# orenge=cv2.dilate(orenge, kernal)
# res3 = cv2.bitwise_and(frame,frame, mask= orenge)


# green=cv2.dilate(green, kernal)
# res4 = cv2.bitwise_and(frame,frame, mask= green)

    white=cv2.dilate(white, kernal)
    res5 = cv2.bitwise_and(frame,frame, mask= white)

# black=cv2.dilate(black, kernal)
# res6 = cv2.bitwise_and(frame,frame, mask= black)






# (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# for pic, contour in enumerate(contours):

#     area = cv2.contourArea(contour)
#     if(area>10000):
#         x,y,w,h = cv2.boundingRect(contour) 
#         frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
#         cv2.putText(frame,"red",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))        
#         print("red")



# (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# for pic, contour in enumerate(contours):

#     area = cv2.contourArea(contour)
#     if(area>10000):
#         x,y,w,h = cv2.boundingRect(contour) 
#         frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
#         cv2.putText(frame,"blue",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))        
#         print("blue")



# (_,contours,hierarchy)=cv2.findContours(orenge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# for pic, contour in enumerate(contours):

#     area = cv2.contourArea(contour)
#     if(area>10000):
#         x,y,w,h = cv2.boundingRect(contour) 
#         frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
#         cv2.putText(frame,"orenge",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))        
#         print("orenge")





# (_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# for pic, contour in enumerate(contours):

#     area = cv2.contourArea(contour)
#     if(area>10000):
#         x,y,w,h = cv2.boundingRect(contour) 
#         frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
#         cv2.putText(frame,"green",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
    
#         print("green")



    (_,contours,hierarchy)=cv2.findContours(white,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):

        area = cv2.contourArea(contour)
        if(area>10000):
            x,y,w,h = cv2.boundingRect(contour) 
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
            cv2.putText(frame,"white",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))
    
            print("white")




# (_,contours,hierarchy)=cv2.findContours(black,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# for pic, contour in enumerate(contours):

#     area = cv2.contourArea(contour)
#     if(area>10000):
#         x,y,w,h = cv2.boundingRect(contour) 
#         frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
#         cv2.putText(frame,"black",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))
    
#         print("black")




# 
    cv2.imshow("test",frame)
    cv2.imshow("res6",res5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
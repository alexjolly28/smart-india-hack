import numpy as np
import cv2


def color(img):    # main_fun


    val = list()   #crat a list variable

    frame = cv2.imread(img)   #read image


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # convert to HSV
    
    #threshold HSV value of red

    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])

    #threshold HSV value of blue


    lower_blue = np.array([105,100,50])
    upper_blue = np.array([140,255,255])

    #threshold HSV value of orenge

 
    lower_orenge = np.array([0,200,255])
    upper_orenge = np.array([30,255,255])

    #threshold HSV value of green


    lower_green = np.array([15,150,200])
    upper_green = np.array([75,255,220])

    #create filter in range

    red = cv2.inRange(hsv, lower_red, upper_red)
    blue = cv2.inRange(hsv, lower_blue, upper_blue)
    orenge = cv2.inRange(hsv, lower_orenge, upper_orenge)
    green = cv2.inRange(hsv, lower_green, upper_green)


    kernal = np.ones((5,5),np.uint8)

    #red filter mask

    red=cv2.dilate(red, kernal)
    res1 = cv2.bitwise_and(frame,frame, mask= red)
    
    #blue filter mask

    blue=cv2.dilate(blue, kernal)
    res2 = cv2.bitwise_and(frame,frame, mask= blue)
   
    #orenge filter mask


    orenge=cv2.dilate(orenge, kernal)
    res3 = cv2.bitwise_and(frame,frame, mask= orenge)

    #green filter mask

    green=cv2.dilate(green, kernal)
    res4 = cv2.bitwise_and(frame,frame, mask= green)




    (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):

        area = cv2.contourArea(contour)
        if(area>8000): #range of ditection
            val.append("RED")

 

    (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):

        area = cv2.contourArea(contour)
        if(area>8000):
            val.append("BLUE")

 
    (_,contours,hierarchy)=cv2.findContours(orenge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):

        area = cv2.contourArea(contour)
        if(area>8000):
            val.append("ORENGE")


    (_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):

        area = cv2.contourArea(contour)
        if(area>8000):
            val.append("GREEN")
        
    return val #return all list

    

print(color('test.jpg'))





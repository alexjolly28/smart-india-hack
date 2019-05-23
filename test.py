import cv2
image = cv2.imread("test.png")
color = int(image[300, 300])
# if image type is b g r, then b g r value will be displayed.
# if image is gray then color intensity will be displayed.
print (color)
import cv2
import matplotlib.pyplot as plt
import numpy

img = cv2.imread("2019VisionImages/RocketPanelStraightDark24in.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(hsv)
plt.show()
mask1 = cv2.inRange(hsv, (65, 200, 200), (85, 255,255))
plt.imshow(mask1)
plt.show()
_, contours, heirarchy = cv2.findContours(mask1.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print("countours:", len(contours))
max1 = 0
max2 = 0
box1 = 0
box2 = 0
for contour in contours:
    rotrect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rotrect)
    box = numpy.int0(box)

    area = cv2.contourArea(box)
    print(area)
    if area > max1:
        max2 = max1
        box2 = box1
        max1 = area
        box1 = box
    elif area > max2:
        max2 = area
        box2 = box

for i in (box1, box2):
    cv2.drawContours(img, [i], 0, (0,0,255), 2)
cv2.imshow("Image", img)
cv2.waitKey(1000)
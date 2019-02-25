import cv2
import matplotlib.pyplot as plt
import numpy as np
import math


img = cv2.imread("2019VisionImages/RocketPanelStraightDark96in.jpg")
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
    box = np.int0(box)

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

x1, x2, x3, x4 = (10000000, 0, 10000000, 0)
for point in box1:
    px, py = point
    x1 = min(x1, px)
    x2 = max(x2, px)

for point in box2:
    px, py = point
    x3 = min(x3, px)
    x4 = max(x4, px)

interval1 = (x1, x2)
interval2 = (x3, x4)
if x2 > x3:
    interval1, interval2 = interval2, interval1
print(interval1, interval2)
print(interval2[0] - interval1[1])


# camera constants (should maybe move to file or list)
diagonal_view_angle = 68.5
diagonal = math.sqrt(320**2 + 240**2)
degrees_per_pixel = diagonal_view_angle / diagonal


width_px = interval2[0] - (interval1[1] + interval2[0]) / 2
width_in = 4
width_angle = math.radians(degrees_per_pixel * width_px)

print("angle:", width_angle)
print("width:", width_px)

distance = width_in / math.tan(width_angle)

print(distance)





for i in (box1, box2):
    cv2.drawContours(img, [i], 0, (0,0,255), 2)
cv2.imshow("Image", img)
cv2.waitKey(1000)
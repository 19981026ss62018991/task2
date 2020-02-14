import cv2
import matplotlib.pyplot as plt


image = cv2.imread("task2_1.png")


image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

lower_R = (0,180,180)
upper_R = (50,255,255)

mask = cv2.inRange(image_hsv, lower_R, upper_R)
result = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)

plt.imshow(result)

plt.show()
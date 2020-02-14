import cv2
import matplotlib.pyplot as plt


image = cv2.imread("task2_3.png")


image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

lower_B = (70,50,0)
upper_B = (130,255,255)

mask = cv2.inRange(image_hsv, lower_B, upper_B)
result = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)

plt.imshow(result)

plt.show()
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt


im= cv2.imread('task2_4.png')
HEIGHT, WIDTH = im.shape[:2]
for x in range(HEIGHT):
    for y in range(WIDTH):
        #print(im[x,y])
        b, g, r = im[x, y]
        if(b, g, r) < (255, 255, 255):
            continue
        im[x, y] = 0, 0, 0
cv2.imwrite('edit.png', im)
im = np.array(Image.open('edit.png'))
im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0

# 横に並べて結合（どれでもよい）
im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)
# im_RGB = np.hstack((im_R, im_G, im_B))
# im_RGB = np.c_['1', im_R, im_G, im_B]

pil_img_RGB = Image.fromarray(im_RGB)
pil_img_RGB.save('task2_3_color.png')
image_hsv_r = cv2.cvtColor(im_R, cv2.COLOR_RGB2HSV)

lower_R = (0, 50, 50)
upper_R = (20, 255, 255)

mask_r = cv2.inRange(image_hsv_r, lower_R, upper_R)
result_r = cv2.bitwise_and(im_R, im_R, mask=mask_r)

plt.imshow(result_r)

plt.show()
image_hsv_g = cv2.cvtColor(im_G, cv2.COLOR_RGB2HSV)

lower_G = (44, 50, 50)
upper_G = (80, 255, 255)

mask_g = cv2.inRange(image_hsv_g, lower_G, upper_G)
result_g = cv2.bitwise_and(im_G, im_G, mask=mask_g)

plt.imshow(result_g)

plt.show()

image_hsv_b = cv2.cvtColor(im_B, cv2.COLOR_RGB2HSV)

lower_B = (70, 50, 50)
upper_B = (130, 255, 255)

mask_b = cv2.inRange(image_hsv_b, lower_B, upper_B)
result_b = cv2.bitwise_and(im_B, im_B, mask=mask_b)

plt.imshow(result_b)

plt.show()
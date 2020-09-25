import numpy as np
import cv2
import pylab as plt

# Read in the image.
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE);

(thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
img = im_bw

cv2.imwrite('bw_image.jpg', im_bw)

dimensions = img.shape
print("Image size : ", dimensions)


# Clear text file
f = open("points.txt", "w")
for x in range(0, dimensions[0], 20):
    for y in range(0, dimensions[1], 20):
        # Write the points to a text file
        if (img[x, y] < 128) and (img[x-1, y] < 128) and (img[x+1, y] < 128) and (img[x, y-1] < 128) and (img[x, y+1] < 128):
            print ("Point : ", x, y, img[x, y])
            f.write("%d %d\n"%(x, y))
            cv2.circle(img,(y,x), 5, (50,50,255), 2)

cv2.imwrite('bw_image_with_circle.jpg', img)

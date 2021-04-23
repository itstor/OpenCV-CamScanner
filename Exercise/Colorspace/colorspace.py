import cv2
import numpy as np

img = cv2.imread(
    'D:\Programming\Kuliah\Magang\ImplementasiOCV\Learning\Colorspace\img.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

show = np.concatenate((img, gray, hsv, hls), axis=1)

cv2.imshow("Result", show)

cv2.waitKey(0)

cv2.destroyAllWindows()

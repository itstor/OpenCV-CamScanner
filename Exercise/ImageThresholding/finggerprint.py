import cv2
import numpy as np

img = cv2.imread(
    'D:\Programming\Kuliah\Magang\ImplementasiOCV\Learning\ImageThresholding\/finggerprint.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((1, 1), np.uint8)
erosion = cv2.erode(th1, kernel, iterations=1)

cv2.imshow("Result", th1)

cv2.waitKey(0)

cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(
    'D:\Programming\Kuliah\Magang\ImplementasiOCV\Exercise\Thresholding\paper.jpg')

img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 11, 2)
ret3, th4 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

show = np.concatenate((th1, th2, th3, th4), axis=1)

cv2.imshow("Result", show)

cv2.waitKey(0)

cv2.destroyAllWindows()

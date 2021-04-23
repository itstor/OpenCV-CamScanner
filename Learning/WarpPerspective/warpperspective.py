import cv2
import numpy as np

img = cv2.imread(
    'D:\Programming\Kuliah\Magang\ImplementasiOCV\Learning\WarpPerspective\card.jpg')

pts1 = np.float32([[683, 96], [938, 237], [460, 459], [719, 607]])
pts2 = np.float32([[0, 0], [300, 0], [0, 500], [300, 500]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

warped = cv2.warpPerspective(img, matrix, (300, 500))

cv2.imshow("Result", warped)

cv2.waitKey(0)

cv2.destroyAllWindows()

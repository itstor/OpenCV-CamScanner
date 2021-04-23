import cv2
import numpy as np

video = cv2.VideoCapture(0)

captured = False


def order(points):
    points = points.reshape((4, 2))
    newPoint = np.zeros((4, 1, 2), dtype=np.int32)

    add = np.sum(points, axis=1)
    diff = np.diff(points, axis=1)

    newPoint[0] = points[np.argmin(add)]
    newPoint[3] = points[np.argmax(add)]
    newPoint[1] = points[np.argmin(diff)]
    newPoint[2] = points[np.argmax(diff)]

    return newPoint


def enhance(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, enhanced = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return enhanced


def capture(frame, paper):
    approx = cv2.approxPolyDP(paper, 0.02 * cv2.arcLength(paper, True), True)

    approx = order(approx)

    pts1 = np.float32(approx)
    pts2 = np.float32([[0, 0], [595, 0], [0, 842], [595, 842]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    warped = cv2.warpPerspective(frame, matrix, (595, 842))

    return warped


while True:
    _, frame = video.read()

    # frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    display = frame.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    paper = max(contours, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(paper)

    cv2.rectangle(display, (x, y), (x+w, y+h), (0, 255, 0), 1)

    cv2.putText(display, "Press C to capture",
                (display.shape[0]//2, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))

    cv2.imshow('Display', display)

    if cv2.waitKey(1) == ord('c'):
        result = capture(frame, paper)
        enhanced = enhance(result)
        captured = True

    if cv2.waitKey(1) == ord('q'):
        break

    if captured:
        cv2.imshow('Original', result)
        cv2.imshow('Enhanced', enhanced)

video.release()
cv2.destroyAllWindows()

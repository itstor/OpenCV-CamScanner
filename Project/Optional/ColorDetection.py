import cv2

video = cv2.VideoCapture(0)

redRange = (0, )

while True:
    rect, frame = video.read()

    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)[:, :, 1]
    hsvcolor = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hsv = cv2.GaussianBlur(hsv, (7, 7), 0)

    _, thresh = cv2.threshold(
        hsv, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    mask = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel, iterations=1)

    edge = cv2.Canny(mask, 100, 100)

    contours, _ = cv2.findContours(
        edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # hsvMask = cv2.bitwise_and(hsv, hsv, mask=contours)
    # print()
    color = str(int(cv2.mean(hsvcolor, mask=mask)[0]))

    for countour in contours:
        if cv2.contourArea(countour) > 1000:
            x, y, w, h = cv2.boundingRect(countour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(frame, (x+w//2, y+h//2), 5, (0, 255, 0), 1)
            cv2.drawContours(frame, contours, -1, (255), 1)
            cv2.putText(frame, color, (x, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
            cv2.putText(frame, str(int(cv2.contourArea(countour))), (x, y-30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))

    # frame = cv2.equalizeHist(frame)

    cv2.imshow('video', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('hsv', hsv)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

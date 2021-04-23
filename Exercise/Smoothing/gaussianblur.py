import cv2

cascPath = "D:\Programming\Kuliah\Magang\ImplementasiOCV\Learning\GaussianBlur\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(
    "D:\Programming\Kuliah\Magang\ImplementasiOCV\Learning\GaussianBlur\/Video2.mp4")

while True:
    _, frame = video_capture.read()

    # frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        blur = cv2.GaussianBlur(frame[y:y+h, x:x+w], (7, 7), 0)
        frame[y:y+h, x:x+w] = blur

    cv2.imshow('Result', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

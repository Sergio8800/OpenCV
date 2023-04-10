import cv2
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    # immg = cv2.imread(frame)
    immg_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(immg_gray)

    for (x, y, w, z) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + z), (0, 0, 255), 1)
    cv2.imshow('camera', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

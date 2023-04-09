import cv2 as cv
import os

path = 'C:/Users/Admin/dwhelper/'
os.chdir(path)
video_file = 'Кармический композит 1 занятие - YouTube.mkv'
cap = cv.VideoCapture(video_file)


if not cap.isOpened():
    print("Error opening Video File.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv.imshow('frame',frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    # if frame is read correctly, ret is True
    if not ret:
        print("Can't retrieve frame - stream may have ended. Exiting..")
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
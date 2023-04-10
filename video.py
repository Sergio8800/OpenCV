import cv2
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
immg = cv2.imread('faces.jpg')
immg_gray = cv2.cvtColor(immg, cv2.COLOR_BGR2GRAY)

faces = face_cascades.detectMultiScale(immg_gray)
# for face in faces:
#     for (x,y,w,h) in face:
#         cv2.rectangle(immg,(x,y),(x+w,y+h),(0,0,255),1)
for (x,y,w,z)in faces:
    cv2.rectangle(immg,(x,y),(x+w,y+z),(0,0,255),1)
print(faces) # fine face and after need rectangle put on pictures = >>>>
cv2.imshow('Window', immg)
cv2.waitKey(0)

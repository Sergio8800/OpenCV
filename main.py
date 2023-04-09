import cv2
immg = cv2.imread('test.jpg')
print(immg.shape)
# immg = cv2.resize(immg,(500,500))
cv2.imshow('Windows', immg)
cv2.waitKey(1000)
cv2.waitKey(500)
cv2.waitKey(0)
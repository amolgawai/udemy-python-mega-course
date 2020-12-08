"""Face detector using opencv """
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Gray", cv2.WINDOW_NORMAL)
cv2.imshow("Gray", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

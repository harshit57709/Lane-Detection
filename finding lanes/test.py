import cv2
import matplotlib.pyplot as plt

def canny(image):


image = cv2.imread("test_image.jpg")
lane_image = image.copy()
canny_image = canny(lane_image)




cv2.imshow("result",lane_image)
cv2.waitKey(0)

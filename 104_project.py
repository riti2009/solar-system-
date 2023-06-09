import cv2
img = cv2.imread("C:/Users/ritia/OneDrive/Desktop/python/PRO-104-OpenCV-Image-Assets-main/solar-system.jpg")




cv2.putText(img, 'sun', (20,300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))
cv2.putText(img, 'mercury', (110,180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))
cv2.putText(img, 'venus', (190,270), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))
cv2.putText(img, 'earth', (300,270), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))
cv2.putText(img, 'mars', (400,270), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))
cv2.putText(img, 'jupiter', (500,90), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))
cv2.putText(img, 'saturn', (720,110), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))
cv2.putText(img, 'uranus', (950, 130), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))
cv2.putText(img, 'neptune', (1080,140), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))


cv2.imshow('output', img)
cv2.waitKey(0)

cv2.imwrite('space.jpg', img)
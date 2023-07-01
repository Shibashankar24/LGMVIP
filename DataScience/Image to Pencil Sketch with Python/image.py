import cv2
image = cv2.imread(r"C:\Users\ASUS\Desktop\internship\img1.jpg")
grey_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur = cv2.GaussianBlur(invert, (111, 111), 0)
invertedblur = cv2.bitwise_not(blur)

sketch_filter = cv2.divide(grey_filter, invertedblur, scale=256.0)
cv2.imwrite("img.jpg", sketch_filter)
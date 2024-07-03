import cv2
import numpy as np
cap = cv2.VideoCapture(
    "/workspaces/tab_extractor/video/Nothing Else Matters - Metallica - Fingerstyle Guitar Tutorial TAB .mp4")

while cap.isOpened():
        ret, frame = cap.read()
        image = frame
# Display the result
        
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray, 50, 200, 1)
        
        contours, hierarchy = cv2.findContours(canny,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        cv2.imwrite('edged.jpg', canny) 
        cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            area = cv2.contourArea(c)
            if area > 600 and area < 1000:
                cv2.drawContours(image, [c], 0, (36,255,12), 2)

        # Display the result
        cv2.imwrite('image.jpg', image)
        cv2.imwrite('canny.jpg', canny) 

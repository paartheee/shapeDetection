# Import all required libs
import numpy as np
import cv2

#Using openCV too reading image
img = cv2.imread("Input Image Path Here")

#converting image into grayscale image
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#setting threshold of gray image
_,thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)

#using a findContours() function
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# list for storing names of shapes
for contour in contours:

    #cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)

    #finding center point of shape
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

# putting shape name at center of each shape
    if len(approx) == 3:
        cv2.putText(img,"Triangle",(x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5,(0, 0, 0))
    elif len(approx) == 4:
        x1,y1,w,h =cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
          cv2.putText(img,"Square",(x, y),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0, 0, 0))
        else:
          cv2.putText(img,"Rectangle",(x, y),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img,"Pentagon",(x, y),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(img,"Star", (x, y),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0, 0, 0))
    else:
        cv2.putText (img,"Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,250,))


# displaying the image after drawing contours
cv2.imshow("shapes", img)
cv2.waitKey()
cv2.destroyAllWindows()
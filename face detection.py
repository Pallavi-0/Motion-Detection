import cv2
#create haar cascade
faceCascade = cv2.CascadeClassifier("C:/anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
#result the image 
image = cv2.imread("C:/Users/Pratibha/Dropbox/My PC (Pratibha-PC)/Documents/my_photo.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#detect faces in the image
face = faceCascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 5)
#draw rectangle around face
for x, y, w, h in face:
    image= cv2.rectangle(image,(x,y), (x+w,y+h), (0, 255, 0), 3)
resized= cv2.resize(image,(int(image.shape[1]/7),int(image.shape[0]/7)))
cv2.imshow("faces found", resized)
cv2.waitKey(0)
cv2.destroyAllwindows()
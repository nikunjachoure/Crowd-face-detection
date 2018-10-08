import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')  # We load the cascade for the face.
 
image = cv2.imread(r"E:\Downloads\crowd.jpg")   # We load the path of the required image
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # We convert the coloured image into gray image
 
faces = face_cascade.detectMultiScale(grayImage,1.001,1)   # We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
 
print(type(faces))

# We write the below code to count the number of faces in the image:
if len(faces) == 0:
    print("No faces found")
 
else:
    print(faces)
    print(faces.shape)
    print("Number of faces detected: " + str(faces.shape[0]))
 
    for (x,y,w,h) in faces:    # For each detected face:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)  # We paint a rectangle around the face.
 
cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)  # We create a rectange on the image to write the no of faces
cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1) #We display the number of faces on the image
 
cv2.imshow('Image with faces',image) ## We display the output image
cv2.waitKey(0) # We wait for the image to be closed 
cv2.destroyAllWindows()  # # We destroy all the windows inside which the images were displayed.

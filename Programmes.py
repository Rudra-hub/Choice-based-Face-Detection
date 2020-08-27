import cv2

i=str(input("Enter Your Choice''im' for image face detection & 'vd' for video face detection '"))

if (i=="im"):
    #The cascade
    cascade_data = cv2.CascadeClassifier(r'C:\Users\Rudra Pratap\Desktop\CSV\haarcascade_frontalface_default.xml')
    # Reading of the input image
    image = cv2.imread(r'C:\Users\Rudra Pratap\Desktop\CSV\images.jpg')
    # Converting into grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = cascade_data.detectMultiScale(grayscale, 1.1, 4)
    # Drawing of rectangle shape around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Displaying the output    
    cv2.imshow('img', image)
    cv2.waitKey()
    
elif (i=="vd"):
    #The cascade
    cascade_data = cv2.CascadeClassifier(r'C:\Users\Rudra Pratap\Desktop\CSV\haarcascade_frontalface_default.xml')
    # To capture video from webcam. 
    cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
    while True:
        # Read the frame
        _, image = cap.read()
        # Converting to grayscale
        grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Detecting the faces
        faces = cascade_data.detectMultiScale(grayscale, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display
        cv2.imshow('img', image)
        k = cv2.waitKey(30) & 0xff
        # Stop if escape key is pressed
        if k==27:
            break
    # Release the VideoCapture object
    cap.release()
    
else:
    # Identifying the invalid input
    print("Invalid Entry") 





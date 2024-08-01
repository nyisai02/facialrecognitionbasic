#first we going to install pip opencv-python and deepface
#opencv use for image processing,for camera
#import cv2 for camera

import cv2
import threading

#import deepface for facial recognition
from deepface import DeepFace
#cv2.videoCapture(0) for webcam (0)is the number of camera 0 mean one camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match=False

#input the image that you want to detect for facial recognition
input_image=cv2.imread("test.jpg")

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame,input_image.copy())["verified"]:
            face_match=True
        else:
            face_match=False
    except ValueError:
        face_match=False
#we will use looping to detect the face in the image is matching or not
#ord() is used to convert a single Unicode character into an integer
while True:
    ret,frame=cap.read()

    if ret:
        if counter %10==0:
            try:
                threading.Thread(target=check_face,args=(frame.copy(),)).start()
            except ValueError:
                pass

        counter+=1

        if face_match:
            cv2.putText(frame,"MATCH",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
        else:
            cv2.putText(frame,"NO MATCH",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
        cv2.imshow("Frame",frame)


    key =cv2.waitKey(1)
    if key==ord('q'):
        break

#cv2.destroyAllWindows() is destorys or close all the windows we created
#
cv2.destroyAllWindows()


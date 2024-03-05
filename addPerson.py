import cv2
import face_recognition
import os
import face_recognition_models
import numpy as np
import dlib
from scipy.spatial import distance
from skimage import io

# Create directory for all photos
if not os.path.exists('./faces'):
    os.mkdir('./faces')

def addPerson(name):

    # Read face 
    cam = cv2.VideoCapture(0) # Default camera device
    _, frame = cam.read() # boolean, image
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    DIR = './faces'

    # Create directory for new person
    if not os.path.exists('./faces/' + str(name)):
        os.mkdir('./faces/' + str(name))

    # Save image and close camera
    cv2.imwrite('./faces/{}/_{}.jpg'.format(name, name), frame)
    print("Image saved")

    cam.release()
    cv2.destroyAllWindows()


name = input("Enter the name of the person: ")

addPerson(name)
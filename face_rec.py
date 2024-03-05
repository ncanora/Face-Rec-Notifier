import dlib
import os
from skimage import io
from scipy.spatial import distance
import numpy as np
import cv2
import dlib
import cv2
path = './faces'

def mainCapture():
    print("Starting Capture...")
    faces = {} # Dictionary to store the names of people and the number of times they were recognized
    faceList = [] # List to store the names of people recognized
    imagePaths = []

    # Walk through each file in the directory/subdirectories
    for root, dirs, files in os.walk(path):
        for file in files:
            face = os.path.join(root, file)
            name = str(file).replace(".jpg", "")
            name = os.path.basename(name)
            name = name.replace("_", "")
            faces[name] = 0
            faceList.append(name)
            faceList.sort()
            imagePaths.append(face)
    
    print("Faces tracked: ", end='')
    print(faceList)

    # Load pre-trained models from dlib
    shape_detector= dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat') 
    facerec = dlib.face_recognition_model_v1('./dlib_face_recognition_resnet_model_v1.dat')

    # Extract the descriptor (the thing that helps recognize faces) from each photo
    face_descriptor = []
    imagePaths.sort()
    dlib_detector = dlib.get_frontal_face_detector()

    # Loop through each image in the directory and create descriptors to compare
    for imagePath in imagePaths:
        img = io.imread(imagePath)

        detect = dlib_detector(img, 1)

        for k, d in enumerate(detect):
            shape = shape_detector(img, d)

        face_descriptor.append(facerec.compute_face_descriptor(img, shape))

    capture = cv2.VideoCapture(0)
    found = False # stop when match is found
    face = ""
    image = 0
    # Loop through webcam image and compare to all descriptors
    while (not found):
        _, img = capture.read()
        image = img
        detector_webcam = dlib_detector(img, 1)
        for k, d in enumerate(detector_webcam):
            shape = shape_detector(img, d)
        
        flag = True
        face_descriptor2 = facerec.compute_face_descriptor(img, shape)
        for i in range (0, len(face_descriptor)):
            a = distance.euclidean(face_descriptor[i], face_descriptor2)
            if a < 0.6:
                print(faceList[i])
                faces[faceList[i]] += 1 # Increase the number of times the person was recognized
                flag = False
            if faces[faceList[i]] >= 3: # If the person was recognized 3 times, we stop the program
                found = True
                face = faceList[i]

        if flag == True:
            print("Unknown")
            
    return face, image
    capture.release()
    cv2.destroyAllWindows()



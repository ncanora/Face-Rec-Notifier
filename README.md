Facial Recognition Notifier
======  
This project uses OpenCV and dlib Facial Recognition models to recognize faces and send a notification via gmail.

## Setup

1. Clone the repository.

2. Install the prerequisites

**Download the pre-trained models and put them in the project directory**

http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2

**Download modules:**
This project requires OpenCV, SciKit-Image, and SciPy. Run the commands below:
~~~
pip3 install opencv-python 
pip3 install scikit-image
pip3 install scipy
~~~   

**Install CMake (WINDOWS USERS)**
https://cmake.org/download/

**Install dlib library**
The dlib libary is required to use the pre-trained models. Clone the dlib repo in the project directory, then install using setup.py:

~~~
git clone https://github.com/davisking/dlib.git
cd dlib
python3 setup.py install
~~~ 

## Usage

To add a person for facial recognition, put them in front of the camera and run addPerson.py
To recognize a face, run main.py
Download your email credentials.json file from gmail and copy to same directory as send.py
Run send.py to allow permissions (first time only) and to send email notifications

## Code Adaptation

The face recognition is adapted from the user [Simple-FaceRec by user SSL0](https://github.com/SSL0/Simple-FaceRec). 

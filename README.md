# Facial-Recognition
detecting faces from imaged or webcam and displaying them using python and opencv2

#how to use :
using a folder containing images:
  place your pictures in the folder images and run photos.py

using your webcam:
  run webcam.py
  if you have more than one webcam and you want to switch to your secondary webcam ,
  change the 0 in camera = cv2.VideoCapture(0) in the detect_from_webcam
  function in the main file to the index of your camera

#Notes:
you can change the used haarcascade by modifying it's path in one of the main files(webcam or photos)
this program is a work in progress so it's still not very accurate and still missing a lot of features

#Screenshots:
using photos folder:
![alt text](https://github.com/zurakin/Facial-Recognition/blob/master/screenshots/obama.png?raw=true)
![alt text](https://github.com/zurakin/Facial-Recognition/blob/master/screenshots/avengers.png?raw=true)

using webcam:
![alt text](https://github.com/zurakin/Facial-Recognition/blob/master/screenshots/webcam.png?raw=true)
![alt text](https://github.com/zurakin/Facial-Recognition/blob/master/screenshots/webcam2.png?raw=true)

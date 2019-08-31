import functions


##haar cascades
face_cascade = functions.load_cascade(r"haar cascade\face\haarcascade_frontalface_alt.xml")
sideface_cascade = functions.load_cascade(r"haar cascade\face\haarcascade_profileface2.xml")


functions.detect_from_webcam(face_cascade)

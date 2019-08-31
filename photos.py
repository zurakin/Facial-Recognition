import functions


##haar cascades
face_cascade = functions.load_cascade(r"haar cascade\face\haarcascade_frontalface_alt.xml")
sideface_cascade = functions.load_cascade(r"haar cascade\face\haarcascade_profileface2.xml")


images = functions.fetch_images("images/","jpg")
functions.detect_from_folder("images",face_cascade)

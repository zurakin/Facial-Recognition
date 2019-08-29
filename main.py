import image
import cv2
import glob

def load_cascade(path):
    return cv2.CascadeClassifier(path)

def fetch_images(path,extention):
    paths = glob.glob(path+"*."+extention)
    return [image.Image(path) for path in paths]

def execute(images,face_cascade):
    for image in images:
        print(image.shape)
        while image.shape[1]> 1024 or image.shape[0] >786:
            image.resize((int(image.shape[1]*0.9),int(image.shape[0]*0.9)))
        image.make_greyscale()
        image.search_faces(face_cascade)
        image.detect_faces()
        image.display(0)

face_cascade = load_cascade(r"haar cascade\haarcascade_frontalface_default.xml")
images = fetch_images("images/","jpg")
execute(images,face_cascade)

import image
import cv2
import glob

def load_cascade(path):
    return cv2.CascadeClassifier(path)

def fetch_images(path,extention):
    paths = glob.glob(path+"*."+extention)
    return [image.Image(path) for path in paths]

def detect_from_folder(folder,face_cascade):
    images = fetch_images(folder+"/","jpg")
    for image in images:
        while image.shape[1]> 1024 or image.shape[0] >786:
            image.resize((int(image.shape[1]*0.9),int(image.shape[0]*0.9)))
        image.make_greyscale()
        image.search_faces(face_cascade)
        image.detect_faces()
        if image.display(1000)== False:
            break
    cv2.destroyAllWindows()

def detect_from_webcam(face_cascade):
    camera = cv2.VideoCapture(0)
    while True:
        check,frame = camera.read()
        frame = image.Image(frame)
        while frame.shape[1]> 1024 or frame.shape[0] >786:
            frame.resize((int(frame.shape[1]*0.9),int(frame.shape[0]*0.9)))
        frame.make_greyscale()
        frame.search_faces(face_cascade)
        frame.detect_faces()
        if frame.display(1)==False:
            break
    camera.release()
    cv2.destroyAllWindows()

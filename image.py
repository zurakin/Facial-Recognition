import cv2

class Image:
    '''
    this class is used to load and modify image ,
    images can be recorded from a webcam or loaded
    from the computer using the path of the image
    '''
    def __init__(self,image):
        if type(image) == str:
            self.path = image
            self.image = cv2.imread(image)
            self.shape = self.image.shape
        else:
            self.image = image
            self.shape = image.shape

    def get_greyscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def make_greyscale(self):
            self.grey = self.get_greyscale()

    def get_resized(self,shape):
        return cv2.resize(self.image,shape)

    def resize(self,shape):
        self.image = self.get_resized(shape)
        self.shape = self.image.shape

    def display(self,time):
        cv2.imshow('facial detection', self.image)
        key = cv2.waitKey(time)
        if key == ord('q'):
            return False


    def search_faces(self,haar_cascade):
        try:
            self.faces = haar_cascade.detectMultiScale(self.grey,
            scaleFactor = 1.1 , minNeighbors = 5)
        except:
            self.faces = haar_cascade.detectMultiScale(self.image,
            scaleFactor = 1.1 , minNeighbors = 5)

    def detect_faces(self):
        temp_img = self.image
        for x,y,w,h in self.faces:
            temp_im = cv2.rectangle(temp_img , (x ,y),(x+w ,y+h),(0,255,0), 3)
        self.image = temp_img

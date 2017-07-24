import cv2
import time

class video_framer(object):
    def __init__(self, path):                       
        self.video_capture = cv2.VideoCapture()     
        self.path = path                            
        self.old_time = time.time()                 

    def get_video_frame(self):
        success, frame = self.video_capture.read()  
        if success:
            return frame                            
        if not self.video_capture.isOpened():       
            self.video_capture.open(self.path)

        else:
            self.video_capture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)  

        frame = self.video_capture.read()[1]        
        return frame

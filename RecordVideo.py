import numpy as np
import cv2
import os 


filename = 'video.avi'
fps = 24
my_res = '500'


def change_res(cap,width,height):
    cap.set(3, width)
    cap.set(4, height)

#minimum dimensions 480p
STD_DIMENSIONS = {
    "480p": (640,480),
    "720p": (1280,720),
    "1080p": (1920,1080),
    "4k": (3840,2160),

}

def get_dims(cap, res ='480p'):
    width,height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    change_res(cap,width,height)
    return width,height

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'), #fourcc countains video codecs (encoding decoding usually for compression) XVID is one of those codecs
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

cap = cv2.VideoCapture(0)
out = cv2.VideoWriter(filename, get_video_type(filename) , fps, get_dims(cap,my_res))

while True:
    ret,frame = cap.read()
    out.write(frame) #complies the frames into a video
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

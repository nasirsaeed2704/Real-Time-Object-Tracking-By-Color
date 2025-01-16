import cv2
import numpy as np
from PIL import Image

################################################################################
#the BGR values of the colors
YELLOW = [0, 255, 255]
GREEN = [0, 255, 0]
BLUE = [255, 0, 0]
PURPLE = [128, 0, 90]
RED = [0, 0, 255]
ORANGE = [0, 90, 180]

#a dictionary of HSV color limits
hsv_color_limits = {
    'YELLOW': {
        'lower': np.array([17, 170, 170], dtype=np.uint8),
        'upper': np.array([35, 255, 255], dtype=np.uint8)},

    'GREEN': {
        'lower': np.array([38, 110, 110], dtype=np.uint8),
        'upper': np.array([78, 255, 255], dtype=np.uint8)},

    'BLUE': {
        'lower': np.array([95, 140, 140], dtype=np.uint8),
        'upper': np.array([125, 255, 255], dtype=np.uint8)},

    'RED': {
        'lower': np.array([175, 140, 140], dtype=np.uint8),
        'upper': np.array([180, 255, 255], dtype=np.uint8)},
    
    'ORANGE': {
        'lower': np.array([175, 140, 140], dtype=np.uint8),
        'upper': np.array([180, 255, 255], dtype=np.uint8)}
}

################################################################################
#function to get the upper and lower limits of the BGR color in HSV
def get_limits(color, range):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
   
    #setting hsv color range
    hue = hsvC[0][0][0]

    #ensuring the hsv in the case of red does not overflow (stays in the range of 0 to 180)
    if hue >= (180 - range): 
        lower_limit = np.array([hue - range, 70, 70], dtype=np.uint8) 
        upper_limit = np.array([180, 255, 255], dtype=np.uint8) 
    elif hue <= range:
        lower_limit = np.array([0, 100, 100], dtype=np.uint8) 
        upper_limit = np.array([hue+range, 255, 255], dtype=np.uint8) 
    else:
        lower_limit = np.array([hue-range, 100, 100], dtype=np.uint8) 
        upper_limit = np.array([hue+range, 255, 255], dtype=np.uint8)
    
    return lower_limit, upper_limit

################################################################################
#function to detect color
def detect_color(img, lower_limit = False, upper_limit = False):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #creating a mask through limits
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    #converting image into pillow and getting the bounding box
    mask_ = Image.fromarray(mask)  
    bbox = mask_.getbbox()  

    #drawing the bounding box
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), 2)
    
    return img  #returning the image after outlining the color in it
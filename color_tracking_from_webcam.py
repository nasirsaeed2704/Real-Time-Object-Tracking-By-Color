import cv2
from utils import hsv_color_limits, detect_color
################################  DRIVER CODE  ##################################
#UNCOMMENT THE COLOR YOU WISH TO DETECT
color = 'YELLOW'
# color = 'BLUE'   
# color = 'RED' 
# color = 'GREEN' 
# color = 'ORANGE'  

# getting the upper and lower bounds of the chosen color
lower =  hsv_color_limits[color]['lower']
upper = hsv_color_limits[color]['upper']

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    frame = detect_color(img=frame, lower_limit=lower, upper_limit=upper)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
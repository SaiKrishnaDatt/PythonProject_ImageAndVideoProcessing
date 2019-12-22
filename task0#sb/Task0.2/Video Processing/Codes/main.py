import cv2
import numpy as np
import os

def partA():
    cap = cv2.VideoCapture('../Videos/RoseBloom.mp4')
    framerate = 25
    framecount = 0

    while(True):
        # Capture frame-by-frame
        success, image = cap.read()
        framecount += 1

        # Check if this is the frame closest to 6 seconds
        if framecount == ((framerate * 6)+1):
          framecount = 0
          cv2.imwrite('../Generated/frame_as_6.jpg',image)
          break;

        # Check end of video
        if cv2.waitKey(1) & 0xFF == ord('q'):
              break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def partB():
    pathv=os.path.join( os.getcwd(), '../Generated', "frame_as_6.jpg" )
    img = cv2.imread(pathv)
    b = img.copy()
    # set green and blue channels to 0
    b[:, :, 0] = 0
    b[:, :, 1] = 0
    cv2.imwrite('../Generated/frame_as_6_red.jpg',b)

partA()
partB()

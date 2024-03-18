import cv2 
def FrameCapture(path): 
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = 1
    while success: 
        success, image = vidObj.read()
        image = cv2.resize(image, (120,90))
        cv2.imwrite("source/frame/%d.jpg" % count, image)
        count += 1
if __name__ == '__main__': 
    FrameCapture("source/video.mp4")
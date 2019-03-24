import cv2
from vvvv_communication import *
import time

source = "rtsp://admin:hk12345678@192.168.1.4/Streaming/Channels/1"

cam = cv2.VideoCapture(source)

cam.set(3, 400)
cam.set(4, 400)

face = cv2.CascadeClassifier('../classifier_machine/haar/face.xml')

IP = '127.0.0.1'
PORT = 4444
name = 'test'

# logger = LogHelper(name='log/VVVV_COMMUNICATION')
# vvvv = VvvvHandle(IP, PORT, name, logger)

while True:
    # time_start = time.time()
    img = cam.read()[1]
    # face_1 = face.detectMultiScale(img, 1.2, 5)
    # for l, t, w, h in face_1:
    #     cv2.rectangle(img, (l, t), (l + w, t + h), (0, 0, 255), 4)

    if img is None:
        print('video is over...')
        break
    cv2.imshow('a', img)
    # print(time.time() - time_start)
    if cv2.waitKey(30) == 27:
        break

# vvvv.close()
cv2.destroyAllWindows()
#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
"""
__title__ = 'None'
__author__ = 'None'
__mtime__ = 'None'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛

┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌
│Esc│   │ F1│ F2│ F3│ F4│ │ F5│ F6│ F7│ F8│ │ F9│F10│F11│F12│ │P/S│S L│P/B│  ┌┐    ┌┐    ┌┐  │
└───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐
│~ `│! 1│@ 2│# 3│$ 4│% 5│^ 6│& 7│* 8│( 9│) 0│_ -│+ =│ BacSp │ │Ins│Hom│PUp│ │N L│ / │ * │ - │   │
├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ 
│ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │{ [│} ]│ | \ │ │Del│End│PDn│ │ 7 │ 8 │ 9 │   │   │
├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴─────┤ 
│ Caps │ A │ S │ D │ F │ G │ H │ J │ K │ L │: ;│" '│ Enter  │                   │ 4  │ 5 │ 6 │   │   │
├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────────┤  
│ Shift  │ Z │ X │ C │ V │ B │ N │ M │< ,│> .│? /│  Shift   │     │ ↑ │       │ 1  │ 2 │ 3 │   │   │
├─────┬──┴─┬─┴──┬┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ 
│ Ctrl│    │Alt │         Space         │ Alt│    │    │Ctrl│ │ ← │ ↓ │ → │ │   0   │ . │←─┘│    │
└─────┴────┴────┴───────────────────────┴────┴────┴────┴────┘ 
"""

from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2


# ap = argparse.ArgumentParser()
# ap.add_argument('-p', '--prototxt', required=True, help="path to Caffe 'deploy' prototxt file")
# ap.add_argument('-m', '--model', required=True, help='path to Caffe pre-trained model')
# ap.add_argument('-c', '--confidence', type=float, default=0.2, help='minimum probability to filter weak detections')
# args = vars(ap.parse_args())

# 设置初始化列表和随机颜色

# label_path = 'F:\\OpenCV\\Light_PANZHOU\\synset_words.txt'

# rows = open(label_path).read().strip().split("\n")
# CLASSES = [r[r.find(" ") + 1:].split(",")[0] for r in rows]

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
 "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
 "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
 "sofa", "train", "tvmonitor"]


COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

CONFIDENCE = 0.2

# 加载模型
prototxt_path = 'F:\\OpenCV\\Light_PANZHOU\\MobileNetSSD_deploy.prototxt.txt'
model_path = 'F:\\OpenCV\\Light_PANZHOU\\MobileNetSSD_deploy.caffemodel'
# net = cv2.dnn.readNetFromCaffe(args['prototxt'], args['model'])
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# vc = VideoStream(src=0).start()
vc = cv2.VideoCapture('F:\\OpenCV\\Light_PANZHOU\\PANZHOU_DATA\\VIDEO_ALL\\v01.mp4')
time.sleep(2.0)
fps = FPS().start()

while True:

    frame = vc.read()[1]
    # frame = np.array(frame, dtype=float)
    (h, w) = frame.shape[:2]
    # print(type(frame))

    start_time = time.time()

    blob = cv2.dnn.blobFromImage(frame, 1.0 / 127.5, (300, 300), (127.5, 127.5, 127.5), True)

    net.setInput(blob)
    detections = net.forward()
    print(time.time()-start_time)
 
    for i in np.arange(0, detections.shape[1]):
        confidence = detections[0, 0, i, 2]

        if confidence > CONFIDENCE:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startx, starty, endx, endy) = box.astype('int')

            label = '{}:{:.2f}%'.format(CLASSES[idx], confidence*100)
            cv2.rectangle(frame, (startx, starty), (endx, endy), COLORS[idx], 2)
            y = starty - 15 if starty - 15 > 15 else starty + 15
            cv2.putText(frame, label, (startx, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx, 2])

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break
    fps.update()

fps.stop()

cv2.destroyAllWindows()
vc.stop()
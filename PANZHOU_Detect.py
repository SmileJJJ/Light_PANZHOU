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

import cv2
import time
import numpy as np
import os

def test_svm(hog):
    test_list = []
    test = os.listdir(r'F:/OpenCV/SVM_HOG_DATA/Test')
    for i in test:
        test_list.append(os.path.join(r'F:/OpenCV/SVM_HOG_DATA/Test', i))
    i = 0
    for f in test_list:
        i += 1
        print(i)
        img = cv2.imread(f,cv2.COLOR_BGR2GRAY)
        rects, _ = hog.detectMultiScale(img, winStride=(4, 4), padding=(8, 8), scale=1.05)
        for (x,y,w,h) in rects:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('{}'.format(i),img)
        if i>=10:
            break
    cv2.waitKey()

def test_svm_vidio(hog):
    source = "rtsp://admin:hk12345678@192.168.1.4/Streaming/Channels/1"
    cap = cv2.VideoCapture(source)
    time_1 = time.time()

    l_set = 1380
    t_set = 20

    w_set = 200
    h_set = 200

    while True:
        time_2 = time.time()
        img = cap.read()[1]

        cv2.rectangle(img, (l_set, t_set), (l_set+w_set, t_set+h_set), (0, 0, 255), 4)
        fram_area = img[t_set:t_set+h_set, l_set:l_set+w_set]

        if img is None:
            print('video is over...')
            print(time.time() - time_1)
            continue

        fram_area = cv2.cvtColor(fram_area, cv2.COLOR_BGR2GRAY)
        rects, wei = hog.detectMultiScale(fram_area, winStride=(4, 4), padding=(8, 8), scale=1.05)
        for (x, y, w, h) in rects:
            cv2.rectangle(fram_area, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('a', img)
        print(time.time() - time_2)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()

hog = cv2.HOGDescriptor()
# hog.load('myHogDector.bin')
#官方自带的检测器
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#两种测试方式：1.测试数据集  2.视频测试
# test_svm(hog)
test_svm_vidio(hog)
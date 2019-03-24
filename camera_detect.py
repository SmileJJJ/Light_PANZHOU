import cv2 as cv
import time
import numpy as np
import matplotlib.pyplot as plt
# import hmmlearn.hmm as hl
import sklearn.preprocessing as ps
import sys

class Video(object):

    def __init__(self,device_num):
        self.video_device = cv.VideoCapture(device_num)
        video_status = self.video_device.isOpened()
        if not video_status:
            sys.exit('设备未找到')

    def set_pixel(self,width,heigth):
        self.video_device.set(3,width)
        self.video_device.set(4,heigth)
        print(self.video_device.get(3),self.video_device.get(4))
        self.video_device.set(10,100)

    def __del__(self):
        self.video_device.release()  # 释放video设备

if __name__ == '__main__':
    source = "rtsp://admin:hk12345678@192.168.1.4/Streaming/Channels/1"
    vc = Video(source)
    # vc.set_pixel(1500, 1500)
    body = cv.CascadeClassifier('../classifier_machine/haar/face.xml')

    hog = cv.HOGDescriptor()
    # hog.load('myHogDector.bin')
    hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

    #0: 120:40
    l_set = 1380
    t_set = 20

    w_set = 400
    h_set = 400

    while True:
        time_1 = time.time()
        fram = vc.video_device.read()[1]
        cv.rectangle(fram, (l_set, t_set), (l_set+w_set, t_set+h_set), (0, 0, 255), 4)
        fram_area = fram[t_set:t_set+h_set, l_set:l_set+w_set]
        # goals = body.detectMultiScale(fram_area, 2.5, 5)
        goals, wei = hog.detectMultiScale(fram_area, winStride=(4, 4), padding=(8, 8), scale=1.05)
        for l, t, w, h in goals:
            cv.rectangle(fram_area, (l, t), (l+w, t+h), (0, 0, 255), 4)
        cv.imshow('video', fram)
        print(time.time() - time_1)
        if cv.waitKey(1) == 27:
            break

    cv.destroyAllWindows()  # 设备在拍摄的时候会加载一些窗口缓冲，销毁(opencv)
'''
 • CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
 • CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
 • CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
 • CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
 • CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
 • CV_CAP_PROP_FPS Frame rate.
 • CV_CAP_PROP_FOURCC 4-character code of codec.
 • CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
 • CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
 • CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
 • CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
 • CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
 • CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
 • CV_CAP_PROP_HUE Hue of the image (only for cameras).
 • CV_CAP_PROP_GAIN Gain of the image (only for cameras).
 • CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
 • CV_CAP_PROP_CONVERT_RGB Boolean flags whether images should be converted to RGB. indicating
 • CV_CAP_PROP_WHITE_BALANCE Currently unsupported
 • CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend cur- rently)
'''
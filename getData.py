import json
import cv2 as cv
import time
import myLogger
import os
import sys

def getdata(path):
    with open(path) as jdata:
        jsonData = json.loads(jdata.read(1024))
        shapeData = jsonData['shapes'][0]
        label = shapeData['label']
        points = shapeData['points']
    return points

def get_all_image(video_path,img_path,Looger):  #video path
    video_count = 0
    image_count = 0
    Looger.writeLog('start to convert...',level="info")
    for video in os.listdir(video_path):
        video_count += 1
        vc = cv.VideoCapture(str(video_path)+str(video))
        vc.set(3, 500)
        vc.set(4, 500)
        while True:
            fram = vc.read()[1]
            if fram is None:
                print('video is over...')
                break
            img_save_path = str(img_path)+str(time.time())+'.png'
            cv.imwrite(img_save_path,fram)
            time.sleep(0.0001)
            image_count += 1
    Looger.writeLog('convert has done,convert {} video and product {} image'.format(video_count,image_count),
                    level="info")

if __name__ == '__main__':
    Loger = myLogger.LogHelper(name='getDate')
    VIDEO_PATH = 'PANZHOU_DATA/VIDEO/'
    IMAGE_PATH = 'PANZHOU_DATA/IMG/'
    get_all_image(VIDEO_PATH,IMAGE_PATH,Loger)

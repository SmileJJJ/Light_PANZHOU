import json
import cv2 as cv
import time
import myLogger
import os
import sys

def pars_json(path):
    with open(path) as jdata:
        jsonData = json.loads(jdata.read(2048))
        shapeData = jsonData['shapes']
        points_list = []
        for i in shapeData:
            label = i['label']
            points = i['points']
            points_list.append(points)
    return points_list

def get_all_image(video_path,img_path,Loger):  #video path
    video_count = 0
    image_count = 0
    Loger.writeLog('start to convert...',level="info")
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
    Loger.writeLog('convert has done,convert {} video and product {} image'.format(video_count,image_count),
                    level="info")

def get_small_img(img,coordinates,img_path):
    count = 0
    for coordinate in coordinates:
        x0 = int(coordinate[0][0])
        y0 = int(coordinate[0][1])
        x1 = int(coordinate[1][0])
        y1 = int(coordinate[1][1])
        new_img = img[y0:y1,x0:x1]
        img_save_path = str(img_path) + str(time.time()) + '.png'
        cv.imwrite(img_save_path,new_img)
        count += 1
    return count

def get_images_path(path):
    path_list = []
    name_list = os.listdir(path)
    for name in name_list:
        path_list.append(str(path)+str(name))
    return path_list


if __name__ == '__main__':
    Loger = myLogger.LogHelper(name='getDate')
    VIDEO_PATH = 'PANZHOU_DATA/VIDEO/'
    IMAGE_PATH = 'PANZHOU_DATA/IMG/'
    JSON_PATH = 'PANZHOU_DATA/JSON'
    SMAILL_IMAGE_PATH = 'PANZHOU_DATA/SMAILL_IMAGE/'
    json_file_01 = 'PANZHOU_DATA/JSON/02.json'

    # get_all_image(VIDEO_PATH,IMAGE_PATH,Loger)
    # coordinates = pars_json(json_file_01)
    # image_path_list = get_images_path(IMAGE_PATH)
    # Loger.writeLog('start to product small image ... ', level="info")
    # image_count = 0
    # for img_path in image_path_list:
    #     img = cv.imread(img_path)
    #     count = get_small_img(img,coordinates,SMAILL_IMAGE_PATH)
    #     image_count += count
    # Loger.writeLog('convert is done ,add {} small image'.format(image_count), level="info")

    # get_pos3_image()

import cv2 as cv
import time
import os

path_f = 'usual_status/'
path_s = 'light_spot/'
path = path_f +path_s

if not os.path.exists(path):
    os.makedirs(path)
    print('------------------------')
    print('create path - {}'.format(path))
    print('------------------------'+'\n'*5)

vc = cv.VideoCapture(0)   #获取摄像头设备
vc.set(3,500)
vc.set(4,500)

time_start = time.time()

while time.time()-time_start < 5:
    fram = vc.read()[1]
    cv.imshow('img',fram)
    cv.waitKey(20)
    cv.imwrite(path+str(time.time())+'.png',fram)

print('\n','img_message--------')
print(vc.get(3))
print(vc.get(4))
print('------------------------')

vc.release()
cv.destroyAllWindows()
import cv2 as cv
import json

def getdata(path):
    with open(path) as jdata:
        jsonData = json.loads(jdata.read(1024))
        shapeData = jsonData['shapes'][0]
        label = shapeData['label']
        points = shapeData['points']
    return points


# img = cv.imread('PANZHOU_VIDEO/222.png')
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('original', img)
# cv.imshow('binary', binary)
# cv.waitKey()

vc = cv.VideoCapture('PANZHOU_VIDEO/v04.mp4')
vc.set(3,500)
vc.set(4,500)
count = 0

[point1,point2] = getdata('PANZHOU_VIDEO/i02.json')

while True:
    vc = cv.VideoCapture('PANZHOU_VIDEO/v04.mp4')
    vc.set(3, 500)
    vc.set(4, 500)
    count = 0
    while True:
        count += 1
        fram = vc.read()[1]
        if fram is None:
            print('video is over...')
            break
        fram = fram[point1[1]:point2[1],point1[0]:point2[0]]
        (B,G,R) = cv.split(fram) #cv.split  多通道分离
        B = cv.equalizeHist(B)
        G = cv.equalizeHist(G)
        R = cv.equalizeHist(R)
        new_image = cv.merge((B,G,R))  #cv.merge  多通道合并
        gray = cv.cvtColor(new_image, cv.COLOR_BGR2GRAY)
        ret, binary = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)
        cv.imshow('img', binary)
        if cv.waitKey(100) == 27:
            break

# gray = cv.cvtColor(fram, cv.COLOR_BGR2GRAY)
# ret, binary = cv.threshold(gray, 250, 255, cv.THRESH_BINARY)

# cv.imwrite('PANZHOU_VIDEO/i02.png',fram)

# cv.waitKey()

print(count)
vc.release()
cv.destroyAllWindows()





# ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)#大律法,全局自适应阈值 参数0可改为任意数字但不起作用
# ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)#TRIANGLE法,，全局自适应阈值, 参数0可改为任意数字但不起作用，适用于单个波峰
# ret, binary = cv.threshold(gray, 251, 255, cv.THRESH_BINARY)# 自定义阈值为150,大于150的是白色 小于的是黑色
# ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)# 自定义阈值为150,大于150的是黑色 小于的是白色
# ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TRUNC)# 截断 大于150的是改为150  小于150的保留
# ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TOZERO)# 截断 小于150的是改为150  大于150的保留
# print("阈值：%s" % ret)
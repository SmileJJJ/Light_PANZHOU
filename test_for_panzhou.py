import cv2 as cv 

img = cv.imread('../../OpenCV/Face_learn/kubeizhenxi.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)#大律法,全局自适应阈值 参数0可改为任意数字但不起作用
# ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)#TRIANGLE法,，全局自适应阈值, 参数0可改为任意数字但不起作用，适用于单个波峰
# ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)# 自定义阈值为150,大于150的是白色 小于的是黑色
# ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)# 自定义阈值为150,大于150的是黑色 小于的是白色
# ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TRUNC)# 截断 大于150的是改为150  小于150的保留
ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TOZERO)# 截断 小于150的是改为150  大于150的保留
print("阈值：%s" % ret)

cv.imshow('original', img)
cv.imshow('binary', binary)
cv.waitKey()
import cv2 as cv 
import numpy as np 
import getData

coords = [(238, 280), [238, 220], (326, 319), [326, 379]]
orginal_image = cv.imread('../../OpenCV/Light_spot_project/usual_status/light_spot/1545360636.4174533.png',cv.IMREAD_GRAYSCALE)
new_image = orginal_image[280:319,238:326]
# cv.fillPoly(new_image,coords,255)
# print(new_image.shape)

# cv.imshow('original',new_image)
# cv.rectangle(orginal_image,coords[0],coords[2],(0,0,255),2)
# cv.imshow('original',orginal_image)
# cv.imshow('original1',new_image)

star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(new_image)

sift = cv.xfeatures2d.SIFT_create()
keypoints,desc = sift.compute(new_image,keypoints)

print(desc)


# cv.waitKey()

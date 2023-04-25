import numpy as np
import os
import math
import cv2
from numpy import random

im = cv2.imread("souris.jpg")
cv2.imshow('image souris', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
h, w, c = im.shape
print(h, w, c)



#Permutation List
def permutation(list):
    list_reverse = []
    for i in reversed(range(len(list))):
        list_reverse.append(list[i])
    return list_reverse

#Image reverse
def image_reverse(im):
    im_reverse = np.zeros(shape=(h, w, c), dtype=np.uint8)
    for i in range(0, h):
        im_reverse[i][:] = permutation(im[i][:])
    return im_reverse

im_reverse = image_reverse(im)

cv2.imshow('image reverse', im_reverse)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('saved_Souris_reverse.jpg', im_reverse)

#image reduce size
def im_reduce(im):
    h, w, c = im.shape
    h1 = int(math.floor(h/2))
    w1 = int(math.floor(w/2))
    im_reduce = np.zeros(shape=(h1, w1, c), dtype=np.uint8)
    for i in range(0, h1):
        for j in range(0, w1):
            #im_reduce[i][j] = im[i*2:i*2+1][j*2:j*2+1].max(axis=(0,1)
            im_reduce[i][j] = im[i*2][j*2]
    return im_reduce
image_reduce = im_reduce(im)
cv2.imshow('image reduce', image_reduce)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('saved_Souris_reduce.jpg', image_reduce)


#image grayscale
def im_gray(im):
    im_gray = np.zeros(shape=(h, w, c), dtype=np.uint8)
    for i in range(0, h):
        for j in range(0, w):
            im_gray[i][j][0:3] = 0.299*im[i][j][0] + 0.587*im[i][j][1] + 0.114*im[i][j][2]
    return im_gray
image_gray = im_gray(im)
cv2.imshow('image grayscale', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('saved_Souris_gray.jpg', image_gray)

def histo(im):
    his = [0]*256
    for i in range(0, h):
        for j in range(0, w):
            his[im[i][j][0]] += 1
    return his

print(histo(im_gray(im)))

def contrast_64(im):
    his_contrast = histo(im)
    for i in range(0, 64, 2):
        his_contrast[i] = his_contrast[i+64]
        his_contrast[255-i] = his_contrast[192-i]
        for l in range(0, h):
            for m in range(0, w):
                if (im[l][m][0] == i+64):
                    im[l][m][0:3] = i
                if (im[l][m][0] == 192 - i):
                    im[l][m][0:3] = 255 - i
    return his_contrast, im

histogram_contrast, image_retouche = contrast_64(im_gray(im))

cv2.imshow('image retouch', image_retouche)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('saved_Souris_Retouch.jpg', image_retouche)

def get_a_b_c_d(im):
    c = 0
    a = 0
    b = 0
    d = 256
    his1 = histo(im)
    for i in range(0, 256):
        if his1[i] < 30:
            a = i
        else: 
            break
    for j in range(255, -1, -1):
        if his1[j] < 30:
            b = j 
        else:
            break
    return a, b, c, d

print(get_a_b_c_d(im_gray(im)))


cv2.imshow('image gray', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


def map_im(im):
    a, b, c, d = get_a_b_c_d(im)
    for color in range(a, b):
        for i in range(0, h):
            for j in range(0, w):
                if (im[i][j][0] == color):
                    color_map = (d - c)/(b-a)*(color - a) + c
                    im[i][j][0:3] = color_map
    return im


cv2.imshow('image map', map_im(image_gray))
cv2.waitKey(0)
cv2.destroyAllWindows()


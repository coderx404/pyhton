import numpy as np 
import cv2 as cv

img =cv.imread('Pemandangan.jpg',1) gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) cv.imshow('grayscale',gray) 

img =cv.imread('Pemandangan.jpg',1) cv.imshow('image',img) 

hsv =cv.cvtColor (img,cv.COLOR_BGR2GRAY) cv.imshow('HSV',hsv) lab = cv.cvtColor(img,cv.COLOR_BGR2LAB) cv.imshow('LAB',lab) 

cv.waitKey(0)

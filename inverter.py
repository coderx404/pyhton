import numpy as np 
import cv2 as cv

citra = cv.imread('Pemandangan.jpg',0) cv.imshow('Hasil Inversi',citra) hasil = citra + 50 cv.imshow('Hasil Inversi',hasil) cv.waitKey(0) cv.destroyAllWindows()

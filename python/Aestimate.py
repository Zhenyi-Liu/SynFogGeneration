import cv2 as cv
import math
import numpy as np


def DarkChannel(im, sz):
    b, g, r = cv.split(im)
    dc = cv.min(cv.min(r, g), b)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (sz, sz))
    dark = cv.erode(dc, kernel)
    return dark

def AtmLight(im, dark):
    [h, w] = im.shape[:2]
    imsz = h * w
    numpx = int(max(math.floor(imsz/1000), 1))
    darkvec = dark.reshape(imsz)
    imvec = im.reshape(imsz, 3)

    indices = np.argsort(darkvec)
    indices = indices[imsz-numpx::]

    atmsum = np.zeros([1, 3])
    for ind in range(1, numpx):
        atmsum = atmsum + imvec[indices[ind]]

    A = atmsum / numpx
    return A


fname = './0324/test.png'
img = cv.imread(fname)
I = img.astype('float64') / 255
dark = DarkChannel(I, 15)
A = AtmLight(I, dark)
A_mean = (A[0, 0] + A[0, 1] + A[0, 2]) / 3
print(A_mean)
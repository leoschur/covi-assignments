#%% imports
import numpy
import cv2 as cv
import matplotlib.pyplot as plt

#%% md
1. Schreiben Sie ein Programm, wo ein Bild eingelesen und mit matplotlib gezeigt wird.
    - Hinweis: OpenCV speichert die Farbkanäle als BGR (Blue Green Red), das muss man zu RGB konvertieren. Sonst sieht Ihr Bild komisch aus.
    - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html

#%%
img: numpy.ndarray = cv.imread('./Linux_logo.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

#%% plot
img[:,:,2]

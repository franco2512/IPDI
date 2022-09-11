import numpy as np
from conversor import *


def raiz_cuadrada(img):
    Y,I,Q = RGBaYIQ(img)
    Y_mod = np.clip(np.sqrt(Y),0,1)
    RGB = YIQaRGB(Y_mod,I,Q)*255
    return RGB

def raiz_cubica(img):
    Y,I,Q = RGBaYIQ(img)
    Y_mod = np.clip(np.cbrt(Y),0,1)
    RGB = YIQaRGB(Y_mod,I,Q)*255
    return RGB


def Cuadrado(img):
    Y,I,Q = RGBaYIQ(img)
    Y_mod = np.clip(np.square(Y),0,1)
    RGB = YIQaRGB(Y_mod,I,Q)*255
    return RGB

def Cubo(img):
    Y,I,Q = RGBaYIQ(img)
    y_m = np.power((Y),3)
    Y_mod = np.clip(y_m,0,1)
    RGB = YIQaRGB(Y_mod,I,Q)*255
    return RGB

def lineal_Trozos(img,maximo,minimo):
    ordenada=0
    abscisa=1
    m=((abscisa - ordenada)/(maximo-minimo))
    b= abscisa - m * minimo
    
    Y,I,Q = RGBaYIQ(img)
    Y_mod = np.zeros(Y.shape)
    
    Y_mod[Y<minimo] = 0
    Y_mod[Y>maximo] = 1
    
    Y_mod = np.where((Y>=minimo)&(Y<=maximo), 1/(maximo-minimo)*(Y-minimo),Y)
    RGB = YIQaRGB(Y_mod,I,Q)*255
    return RGB
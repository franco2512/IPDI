import sys
from turtle import ycor
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import imageio
import numpy as np
import matplotlib.pyplot as plt
#Funciones ipdi
from aritmetica_pixeles import *
from conversor import RGBaYIQ, YIQaRGB



class pantalla (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz_tp2.ui", self)

        rgb = imageio.imread('imageio:astronaut.png')
        rgb = np.minimum(rgb, 255)
        rgb = np.maximum(rgb, 0)
        h, w, _ = rgb.shape
        im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                          w, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(im)
        self.imagen1.setPixmap(pix)

        rgb = imageio.imread('imageio:coffee.png')
        rgb = np.minimum(rgb, 255)
        rgb = np.maximum(rgb, 0)
        h, w, _ = rgb.shape
        im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                          w, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(im)
        self.imagen2.setPixmap(pix)

        self.aplicar.clicked.connect(self.getItem)

    def getItem(self):
        opc = self.opciones.currentText()
        img = realizarOperacion(opc)
        mostrarResultado(self, img)


def mostrarResultado(self, img):

    rgb = img*255
    rgb = np.minimum(rgb, 255)
    rgb = np.maximum(rgb, 0)
    h, w, _ = rgb.shape
    im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                      w, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap.fromImage(im)
    self.imagen3.setPixmap(pix)


def realizarOperacion(opc):
    if opc == "Suma Clampeada RGB":
        return cuasiSumaRGB_Clamp(img1, img2)
    else:
        if opc == "Resta Clampeada RGB":
            return cuasiRestaRGB_Clamp(img1, img2)
        else:
            if opc == "Suma Promediada RGB":
                suma_prom = (img1 + img2)/2
                return suma_prom
            else:
                if opc == "Resta Promediada RGB":
                    resta_prom = (img1 - img2)/2 + 0.5
                    return resta_prom
                else:
                    if opc == "Suma Clampeada YIQ":
                        return sumaYIQClam(img1, img2)
                    else:
                        if opc == "Suma Promedida YIQ":
                            return sumaYIQProm(img1, img2)
                        else:
                            if opc == "Resta Clampeada YIQ":
                                return restaYIQClam(img1, img2)
                            else:
                                if opc == "Resta Promediada YIQ":
                                    return restaYIQProm(img1, img2)
                                else:
                                    if opc == "IF-Darker":
                                        return YIQifdarker(img1, img2)
                                    else:
                                        if opc == "IF-Lighter":
                                            return YIQiflighter(img1, img2)
                                        else:
                                            if opc == "Producto":
                                                (RC, GC, BC) = Producto(img1, img2)
                                                RCGCBC = np.stack(
                                                (RC, GC, BC), axis=2)
                                                RCGCBC = (RCGCBC*255).astype(int)
                                                return(RCGCBC)
                                            else:
                                               if opc == "Cociente":
                                                   (RC,GC,BC) = Cociente(img1, img2)
                                                   RCGCBC = np.stack((RC, GC, BC), axis=2)
                                                   RCGCBC = (RCGCBC).astype(int)
                                                   return(RCGCBC)



img1 = imageio.imread('imageio:coffee.png')[:, 50:550, :]/255
img2 = imageio.imread('imageio:astronaut.png')[56:456, 6:506, :]/255


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = pantalla()
    GUI.show()
    sys.exit(app.exec_())

from fileinput import filename
import sys
from turtle import ycor
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage,QPixmap
import imageio
import numpy as np
import matplotlib.pyplot as plt
#Funciones ipdi
from Operaciones import *
from conversor import *
import cv2
class pantalla(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz_tp3.ui", self)
        self.setWindowTitle("TRABAJO PRACTICO N°3 IPDI- Franco Jonatan Angel Rodriguez")         
        self.btn_cargarImagen.clicked.connect(self.seleccionarImagen)
        self.btn_aplicarFiltro.clicked.connect(self.getItem)
        self.buttonEliminar.clicked.connect(lambda: self.labelImagen.clear())
        self.buttonEliminar_2.clicked.connect(lambda: self.labelImagen_2.clear())
        self.buttonGuardar.clicked.connect(self.guardarImagen)
        

    def seleccionarImagen(self):
        global img
        ruta = QtWidgets.QFileDialog.getOpenFileName(self,'Abrir una imagen','',"Images (*.png *.bmp)")
        img = imageio.imread(ruta[0])[:,:,0:3]
        mostrarImagen(self,img)
        


    def getItem(self):
        opc = self.opcCombo.currentText()
        if opc == "Raiz Cuadrada":
            imgRaiz = raiz_cuadrada(img)
            mostrarImagen2(self,imgRaiz)        
        else:
            if opc == "Cuadrado":
                imgCuad = Cuadrado(img)
                mostrarImagen2(self,imgCuad)
            else:
                if opc == "Raiz Cubica":
                    imgRaizCub = raiz_cubica(img)
                    mostrarImagen2(self,imgRaizCub)
                else:
                    if opc == "Cubo":
                        imgCubo = Cubo(img)
                        mostrarImagen2(self,imgCubo)
                    else:
                        if opc == "Lineal a Trozos":
                            y_min = 0.2
                            y_max = 0.8
                            imgLineal = lineal_Trozos(img,y_max,y_min)
                            mostrarImagen2(self,imgLineal)
                            
    def guardarImagen(self):
        if len(self.filename)!=0:
            filename =  QFileDialog.getSaveFileName(filter= "PNG(*.png);;BMP(*.bmp)")[0]
            cv2.imwrite(filename, self.img)

                
def mostrarImagen(self, rgb):
    rgb = np.clip(rgb, 0, 255)
    h, w, _ = rgb.shape
    im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                      w, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap.fromImage(im)
    self.labelImagen.setPixmap(pix)
    
 

def mostrarImagen2(self, rgb):
    global im
    rgb = np.clip(rgb, 0, 255)
    h, w, _ = rgb.shape
    im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                      w, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap.fromImage(im)
    self.labelImagen_2.setPixmap(pix)

                                                                                  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = pantalla()
    GUI.show()
    sys.exit(app.exec_())
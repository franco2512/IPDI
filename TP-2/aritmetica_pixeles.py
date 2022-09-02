import imghdr
import numpy as np
from conversor import RGBaYIQ, YIQaRGB


def cuasiSumaRGB_Clamp(img1, img2):
    c = np.clip(img1 + img2, 0, 1)
    return c


def cuasiRestaRGB_Clamp(img1, img2):
    c = np.clip(img1 - img2, 0, 1)
    return c


def restaYIQClam(img1, img2):
    YA, IA, QA = RGBaYIQ(img1)
    YB, IB, QB = RGBaYIQ(img2)

    YC = np.maximum(YA - YB, 0)
    IC = (YA*IA-YB*IB)/(YA+YB)
    QC = (YA*QA-YB*QB)/(YA+YB)
    img = YIQaRGB(YC, IC, QC)*255
    return (img)


def restaYIQProm(img1, img2):
    YA, IA, QA = RGBaYIQ(img1)
    YB, IB, QB = RGBaYIQ(img2)

    YC = (YA-YB)*0.5
    IC = (YA*IA-YB*IB)/(YA+YB)
    QC = (YA*QA-YB*QB)/(YA+YB)
    img = YIQaRGB(YC, IC, QC)*255
    return (img)


def sumaYIQClam(img1, img2):

    YA, IA, QA = RGBaYIQ(img1)
    YB, IB, QB = RGBaYIQ(img2)

    YC = (YA+YB)
    IC = ((YA*IA+YB*IB)/(YA+YB))
    QC = ((YA*QA+YB*QB)/(YA+YB))

    imgC = YIQaRGB(YC, IC, QC)
    return(imgC/255)


def sumaYIQProm(img1, img2):
    YA, IA, QA = RGBaYIQ(img1)
    YB, IB, QB = RGBaYIQ(img2)

    YC = (YA+YB)/2
    IC = (YA*IA+YB*IB)/(YA+YB)
    QC = (YA*QA+YB*QB)/(YA+YB)

    imgC = YIQaRGB(YC, IC, QC)
    return(imgC/255)


def YIQifdarker(img1, imgBmod):
    YA, IA, QA = RGBaYIQ(img1)
    YB, IB, QB = RGBaYIQ(imgBmod)

    YC = np.zeros([img1.shape[0], img1.shape[1]])
    IC = np.zeros([img1.shape[0], img1.shape[1]])
    QC = np.zeros([img1.shape[0], img1.shape[1]])

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            if YA[i, j] >= YB[i, j]:
                YC[i, j] = YB[i, j]
                IC[i, j] = IB[i, j]
                QC[i, j] = QB[i, j]
            else:
                YC[i, j] = YA[i, j]
                IC[i, j] = IA[i, j]
                QC[i, j] = QA[i, j]

    imgC = YIQaRGB(YC, IC, QC)
    return(imgC/255)


def YIQiflighter(img1, img2):
    YA, IA, QA = RGBaYIQ(img1)
    YB, IB, QB = RGBaYIQ(img2)

    YC = np.zeros([img1.shape[0], img1.shape[1]])
    IC = np.zeros([img1.shape[0], img1.shape[1]])
    QC = np.zeros([img1.shape[0], img1.shape[1]])

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            if YA[i, j] >= YB[i, j]:
                YC[i, j] = YA[i, j]
                IC[i, j] = IA[i, j]
                QC[i, j] = QA[i, j]
            else:
                YC[i, j] = YB[i, j]
                IC[i, j] = IB[i, j]
                QC[i, j] = QB[i, j]

    imgC = YIQaRGB(YC, IC, QC)
    return(imgC/255)


def Producto(img1, img2):

    RA = img1[:, :, 0]
    GA = img1[:, :, 1]
    BA = img1[:, :, 2]

    RB = img2[:, :, 0]
    GB = img2[:, :, 1]
    BB = img2[:, :, 2]

    RA = np.clip(RA, 0, 255)
    GA = np.clip(GA, 0, 255)
    BA = np.clip(BA, 0, 255)

    RB = np.clip(RB, 0, 255)
    GB = np.clip(GB, 0, 255)
    BB = np.clip(BB, 0, 255)

    RC = np.multiply(RA, RB)
    GC = np.multiply(GA, GB)
    BC = np.multiply(BA, BB)

    return(RC, GC, BC)


def Cociente(img1, img2):

    RA = img1[:, :, 0]
    GA = img1[:, :, 1]
    BA = img1[:, :, 2]

    RB = img2[:, :, 0]
    GB = img2[:, :, 1]
    BB = img2[:, :, 2]



    RC = np.divide(RA, RB).astype(int)
    GC = np.divide(GA, GB).astype(int)
    BC = np.divide(BA, BB).astype(int)

    return(RC, GC, BC)

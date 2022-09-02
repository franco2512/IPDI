import imghdr
import numpy as np

#Convertimos de RGB a YIQ
def RGBaYIQ(img):
#Normalizamos los valores RGB de 0 a 1  
  r = img[:,:,0]
  g = img[:,:,1]
  b = img[:,:,2]
  
  r = np.clip(r,0,255)
  g = np.clip(g,0,255)
  b = np.clip(b,0,255)
  
  Y = (r*0.299+g*0.587+b*0.114)
  I = (r*0.595716-g*0.274453-b*0.321263)
  Q = (r*0.211456-g*0.522591+b*0.311135)
  
  Y = np.clip(Y,0.0,1.0)
  I = np.clip(I,-0.5957,0.5957)  
  Q = np.clip(Q,-0.5226,0.5226)
  
  return(Y,I,Q)

#Convertimos de YIQ a RGB 
def YIQaRGB(Y,I,Q):
#Verificamos que los valores YIQ esten dentro del rango 
 Y = np.clip(Y,0.0,1.0)
 I = np.clip(I,-0.5957,0.5957)  
 Q = np.clip(Q,-0.5226,0.5226)
 
 dimension = Y.shape
        
 r = (Y+0.9563*I+0.621*Q)*255
 g = (Y-0.2721*I-0.6474*Q)*255
 b = (Y-1.1070*I+1.7046*Q)*255
    
 r = np.clip(r,0,255)
 g = np.clip(g,0,255)
 b = np.clip(b,0,255)
 
 img = np.zeros((dimension[0],dimension[1],3),dtype = 'uint8') #Transformo a tipo de dato uint8 ya que es el requerido para mostrar las imágenes
 img[:,:,0] = r
 img[:,:,1] = g
 img[:,:,2] = b
 return(img)


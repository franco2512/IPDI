import numpy as np

# Convierte RGB a YIQ
def RGBaYIQ(img):
    img = np.clip(img/255,0,1)
    
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]
    
    Y = (r*0.299+g*0.587+b*0.114)
    I = (r*0.595716-g*0.274453-b*0.321263)
    Q = (r*0.211456-g*0.522591+b*0.311135)
    
    Y = np.clip(Y,0.0,1.0)
    I = np.clip(I,-0.5957,0.5957)  
    Q = np.clip(Q,-0.5226,0.5226)  
      
    return (Y, I, Q)

# Convierte YIQ a RGB
def YIQaRGB(Y,I,Q):
#Verificamos que los valores YIQ esten dentro del rango 
    Y = np.clip(Y,0.0,1.0)
    I = np.clip(I,-0.5957,0.5957)  
    Q = np.clip(Q,-0.5226,0.5226)
    
    r = (Y+0.9563*I+0.621*Q)
    g = (Y-0.2721*I-0.6474*Q)
    b = (Y-1.1070*I+1.7046*Q)

    img = np.zeros((np.shape(Y)[0], np.shape(Y)[1], 3))
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return np.clip(img,0,1)

   
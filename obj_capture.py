#Codigo que nos sirve para cargar poder capturar nuestra data tanto para objetos ositivos como negativos
#Referencia: https://www.youtube.com/watch?v=v_cwOq06g9E
import cv2
import numpy as np
import imutils #tambien se puede usar cv2
import os

#Definimos Data la cual contiene los archivos pertenecientes a p
Data = 'p'
#En caso no exista la creamos
if not os.path.exists(Data):
    print('Carpeta creada:', Data)
    os.makedirs(Data)

#Definimo la entrada para la camara
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

#Dibujamos las dimensiones del rectangulo que contendrá el objeto
x1,y1 = 190,80
x2,y2 = 450,398

#Definimos una variable para poder guardar cada imagen el objeto a detectar y el fondo
count = 0

while True:
    ret, frame = cap.read()
    if ret == False: break

    #Definimos la copia de frame para poder capturar la seccion de la imagen capturada por el rectangulo
    imAux = frame.copy()

    #Dibujamos el rectangulo que contendra al objeto
    cv2.rectangle(frame,(x1,y1,),(x2,y2),(255,0,0),2)

    objeto = imAux[y1:y2,x1:x2]
    objeto = imutils.resize(objeto, width=38)

    

    k = cv2.waitKey(1)

    #Definimos la tecla que nos permitirá guardar la captura en la carpeta correspondiente
    if k == ord('s'):
            cv2.imwrite(Data+'/objeto_{}.jpg'.format(count),objeto)
            print('Imagen almacenada: ', 'objeto_{}.jpg'.format(count))
            count = count + 1
    if k == 27: break
        
    cv2.imshow('Practica Calificada 5 - Bazan',frame)
    cv2.imshow('Objeto Capturado',objeto)
    
cap.release()
cv2.destroyAllWindows()
#Codigo que nos sirve para cargar el xml y la deteccion de el objeto que queremos
#Referencia: https://www.youtube.com/watch?v=v_cwOq06g9E
import cv2

#Definimo la entrada para la camara
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

#Cargamos nuestro xml del objeto a clasificar
Objet_Classif = cv2.CascadeClassifier('cascade_correct.xml')


while True:
	
    #Leemos cada fotorgrama
	ret,frame = cap.read()
	#Lo clasificamos a escala de grises
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Almacenamos toda las detecciones
	toy = Objet_Classif.detectMultiScale(gray,
	#Parámetro que especifica cuánto se reduce el tamaño de la imagen en cada escala de imagen
	scaleFactor = 6,
	#Parámetro que especifica cuántos vecinos debe tener cada rectángulo candidato para retenerlo
	minNeighbors = 91,
	#tamaño mínimo posible del objeto. Los objetos más pequeños que eso se ignoran
	minSize=(70,78)
    )

	for (x,y,w,h) in toy:
		# cargamos las detecciones almacenadas de toy en x,y,w y h
        #Asi mismo el ancho y alto
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		cv2.putText(frame,'Objeto Detectado',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

	cv2.imshow('Practica Calificada 5 - Bazan',frame)
	
	if cv2.waitKey(1) == 500:
		break
cap.release()
cv2.destroyAllWindows()
import cv2 
imagen = cv2.imread('auroraa.jpg') 
flip1 = cv2.flip(imagen,1) 
cv2.imshow('flip1',flip1) 
cv2.waitKey(0)
#creo que me faltaba una a

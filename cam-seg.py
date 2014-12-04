#!/usr/bin/python

import numpy as np
import cv2, cv, time

### FUNCTIONS

def comprobarFichero():
  
  archivo = "/path/a/algun/fichero"
  
  try: 
    fichero = open(archivo) 
    fichero.close()
    existe = True 
  except: 
    existe = False
    
  return existe

def cerrar():
  
  archivo = "stop"
  
  try:
    fichero = open(archivo)
    fichero.close()
    existe = True
  except:
    existe = False
    
  return existe


### MAIN

tamanoMax = 400
movimiento = False

cam = cv2.VideoCapture(0)

for x in range(100):
  ret, frame = cam.read()
  
fgbg = cv2.BackgroundSubtractorMOG()

while True:
  ret, frame = cam.read()
  
  if ret == True:
    frame = cv2.resize(frame, (tamanoMax,tamanoMax))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    blur = cv2.blur(gray,(10,10))
    
    fgmask = fgbg.apply(blur) # Aplicamos la mascara
    
    columnas = cv2.reduce(fgmask,0,cv.CV_REDUCE_MAX)
    filas = cv2.reduce(fgmask,1,cv.CV_REDUCE_MAX)
    
    for x in range(len(columnas[0])):
      if columnas[0][x] > 0:
	movimiento = True
	break
    if movimiento == False:
      for x in range(len(filas)):
	if filas[x,0] > 0:
	  movimiento = True
	  break
    
    if movimiento == True and comprobarFichero():
      nombre = time.strftime("%y%m%d-%H:%M:%S")+".jpg"
      path="/path/donde/guardar/imagenes/"+nombre
      cv2.imwrite(path,frame)
    
    movimiento = False
      
    if cerrar():
      break

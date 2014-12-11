<h1>Sensor de Movimiento</h1>

IMPORTANTE: Se está desarrollando un makefile que instala todo lo necesario para poder ejecutar el programa, en estos días estará listo.

Autor: José Manuel Rodríguez Montes

Código python para detectar movimiento.
Usando una raspberry pi y una cámara web podemos tener una cámara de vigilancia.

**Es necesario instalar las librerías OpenCV para Python.** Para ello puedes seguir esta guía de Robert Castle: http://robertcastle.com/2014/02/installing-opencv-on-a-raspberry-pi/

**Otro programa necesario es ffmpeg** para la creación de videos a partir de imágenes:
   sudo apt-get install ffmpeg

<h3>Parámetros a configurar</h3>

* archivo --> donde se encuentra el archivo/s que cree un sensor de movimiento. En la funcion cerrar donde se crea el fichero que cierra finaliza la ejecucion del programa.
* tamanoMax --> el tamaño que queremos para nuestras imágenes, esto dependerá de lo buena que sea su cámara.
* nombre --> los nombres que tendrán las imagenes guardadas, por defecto es la fecha y hora del sistema.
* path --> donde guardar las imágenes.

<h3>Funcionamiento</h3>

* Para iniciarlo: Ejecutar el script seguridad.rpi con la opción start
* Para finalizarlo: Ejecutar el script seguridad.rpi con la opción stop


<h3>Datos Adicionales</h3>

El programa puede funcionar con o sin la funcion comprobarFichero(). Si donde vamos a colocar la cámara tenemos algún otro sensor, con comprobarFichero() los podríamos tener sincronizados; por ejemplo: sensor de apertura de puerta crea fichero, el programa solo guardaría imágenes en caso de existir este fichero.
El problema está en que los cambios de luz se detectan también como movimiento, por ello se recomienda tener otro sensor o en su defecto colocar la cámara en un lugar donde no se produzcan cambios de luz.

<h1>Motion Sensor</h1>

**IMPORTANT:** A makefile to install all needed things are been created at this time. It will soon be available.

Author: José Manuel Rodríguez Montes

Python code for detect movement.
Using a raspberry pi with a webcam we obtain a surveillance camera.

**It's necesary install OpenCV libs for Python.** For that you can follow this steps of Robert Castle: http://robertcastle.com/2014/02/installing-opencv-on-a-raspberry-pi/

**Another program you need is ffmpeg** for convert the images into a video:
   sudo apt-get install ffmpeg

<h3>Configuration parameters</h3>

* archivo --> path where is the file created by another sensor. In cerrar/close function the path where the file create to terminate execution.
* tamanoMax --> size we want save images, it's depends on how good your camera is.
* nombre --> name of images. Default: actaul date of your system.
* path --> path where you want to save the images.

<h3>How to running</h3>

* Start: Execute script seguridad.rpi whit start option.
* End: Execute script seguridad.rpi with stop option.

<h3>Additional data</h3>

This program can work with comprobarFichero() function or not. This function is only use to synchronize the program with other sensor, like a motion sensor. We use this because the program can detect the changes of lights like a motion, so we need another sensor to detect, for example, if a door was opened, then, this sensor create a file that allows the camera to takes pictures. 

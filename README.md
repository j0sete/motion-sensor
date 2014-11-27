Autor: José Manuel Rodríguez Montes

Código python para detectar movimiento.
Usando una raspberry pi y una cámara web podemos tener una cámara de vigilancia.

****Es necesario instalar las librerías OpenCV para Python.****

Parámetros a configurar:
	- archivo --> donde se encuentra el archivo/s que cree un sensor de movimiento.
	- tamanoMax --> el tamaño que queremos para nuestras imágenes, esto dependerá de lo buena que sea su cámara.
	- nombre --> los nombres que tendrán las imagenes guardadas, por defecto es la fecha y hora del sistema.
	- path --> donde guardar las imágenes.

El programa puede funcionar con o sin la funcion comprobarFichero().
Si donde vamos a colocar la cámara tenemos algún otro sensor, con comprobarFichero() los podríamos tener sincronizados.
Ejemplo: sensor de movimiento crea fichero, el programa solo guardaría imágenes en caso de estar este fichero.
El problema está en que los cambios de luz se detectan también como movimiento.

-------------------------------------------

Author: José Manuel Rodríguez Montes

Python code for detect movement.
Using a raspberry pi with a webcam we obtain a surveillance camera.

****It's necesary install OpenCV libs for Python.****

We need to configure the next parameters:

	- archivo --> path where is the file created by another sensor.
	- tamanoMax --> size we want save images, it's depends on how good your camera is.
	- nombre --> name of images. Default: actaul date of your system.
	- path --> path where you want to save the images.

This program can work with comprobarFichero() function or not. This function is only use to synchronize the program with other sensor, like a motion sensor. We use this because the program can detect the changes of lights like a motion, so we need another sensor to detect the movement and then the camera takes the pictures.
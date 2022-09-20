from distutils import extension
from fileinput import filename
import os
import shutil #Ayuda a automatizar el proceso de copia y eliminación de archivos y directorios. 

#crea una variable que almacene la ruta del directorio que queremos organizar
path = input('Enter Path: ')

#crea una variable que tenga la lista de archivos
files = os.listdir(path)

# recorramos todos los archivos 
for file in files:
    #dividamos el nombre del archivo y su extension
    filename, extension = os.path.splitext(file)
    
    #eliminamos el punto de la extension
    extension = extension[1:]

    #clasificamos los archivos y lo almacenamos es su repectivo directorio
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        #creamos el directorio sino existe y movemos el archivo a El
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

        #C:/Users/'Jeinfferson B'/Downloads/prueba
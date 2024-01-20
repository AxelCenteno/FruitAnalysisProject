import os
import matplotlib.pyplot as plt
import cv2 as cv

def show_image(color_images, gray_images):
    plt.figure(figsize=(15,10))
    i = 1
    
    for image in color_images:
        plt.subplot(2,len(color_images),i)
        plt.imshow(image[:,:,::-1])
        i += 1
    
    for image in gray_images:
        plt.subplot(2,len(color_images),i)
        plt.imshow(image, cmap = 'gray')
        i += 1
    plt.show()
    
    
def show_gray_image(gray_images):
    plt.figure(figsize=(15,5))
    i = 1
    for image in gray_images:
        plt.subplot(1,len(gray_images),i)
        plt.imshow(image, cmap = 'gray')
        i += 1
    plt.show()
    
def cargar_imagenes(carpeta_imagenes):
    # Obtén la lista de archivos en la carpeta
    archivos = os.listdir(carpeta_imagenes)

    # Filtra los archivos para obtener solo las imágenes
    imagenes = [archivo for archivo in archivos if archivo.endswith('.png')]
    imagen = []
    # Carga cada imagen y realiza las operaciones necesarias
    for imagen_nombre in imagenes:
        ruta_imagen = os.path.join(carpeta_imagenes, imagen_nombre)
        # Carga la imagen
        imagen.append(cv.imread(ruta_imagen))
    return imagen





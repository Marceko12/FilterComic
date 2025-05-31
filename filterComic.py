import cv2
import numpy as np

# Cargar imagen
imagen = cv2.imread('rick.png')
if imagen is None:
    print("Error: No se pudo cargar la imagen")
    exit()

# 1. Suavizar colores con filtro bilateral (parece más dibujo)
imagen_suave = cv2.bilateralFilter(imagen, d=9, sigmaColor=200, sigmaSpace=200)

# 2. Convertir a escala de grises para detectar bordes
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 3. Detectar bordes con Canny
bordes = cv2.Canny(imagen_gris, 50, 150)

# 4. Invertir los bordes (para que el fondo sea blanco)
bordes_inv = cv2.bitwise_not(bordes)

# 5. Convertir bordes a 3 canales
bordes_color = cv2.cvtColor(bordes_inv, cv2.COLOR_GRAY2BGR)

# 6. Combinar la imagen suavizada con los bordes
imagen_comic = cv2.bitwise_and(imagen_suave, bordes_color)

# Mostrar imágenes
cv2.imshow('Original', imagen)
cv2.imshow('Comic', imagen_comic)
cv2.resizeWindow('Original', 600, 800)
cv2.resizeWindow('Comic', 700, 800)

cv2.waitKey(0)
cv2.destroyAllWindows()



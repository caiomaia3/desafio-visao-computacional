# Autor: Caio Maia - caiomaia3@gmail.com
#  Este script tem o objetivo de experimentar as funções básicas do open-cv
import cv2
import numpy as np
from skimage import io

#imgDeTeste = io.imread("/home/senai/Projects/Active/desafio-visao-computacional/img/cards.jpg")
imgDeTeste = io.imread("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Animais_serra_da_canastra_gavi%C3%A3o_carcar%C3%A1_IMG_4868.jpg/800px-Animais_serra_da_canastra_gavi%C3%A3o_carcar%C3%A1_IMG_4868.jpg")

imgDeTeste = cv2.cvtColor(imgDeTeste,cv2.COLOR_BGR2RGB)
print("Imagem em RGB")
cv2.imshow('myImage',imgDeTeste)
cv2.waitKey(0) 
cv2.destroyAllWindows()
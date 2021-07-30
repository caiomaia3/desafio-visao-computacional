#  Este script tem o objetivo de experimentar as funções básicas do open-cv
import cv2
import numpy as np
from skimage import io

#imgDeTeste = io.imread("/home/senai/Projects/Active/desafio-visao-computacional/img/cards.jpg")
imgDeTeste = io.imread("https://www.murtazahassan.com/wp-content/uploads/2020/03/lena.png")
imgDeTeste = cv2.cvtColor(imgDeTeste,cv2.COLOR_BGR2RGB)
print("Imagem em RGB")
cv2.imshow('myImage',imgDeTeste)
cv2.waitKey(0) 
cv2.destroyAllWindows()
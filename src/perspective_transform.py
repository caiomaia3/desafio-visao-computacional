#  Autor: Caio Maia - caiomaia3@gmail.com
#  Este script tem o objetivo de experimentar as funções básicas do open-cv
import cv2
import numpy as np
# from numpy.lib.utils import source
from skimage import io
import my_functions as mf

imported_image = io.imread("/home/senai/Projects/Active/desafio-visao-computacional/img/cards.jpg")
imported_image = cv2.cvtColor(imported_image,cv2.COLOR_BGR2RGB)

source_oclock_points = np.float32([[111,217],
        [289,184],
	[154,483],
	[355,439]])

cv2.imshow('myImage2',mf.card_trasnform(imported_image,source_oclock_points))
cv2.waitKey(0) 
cv2.destroyAllWindows()

#  Autor: Caio Maia - caiomaia3@gmail.com
#  Este script tem o objetivo de experimentar as funções básicas do open-cv
import cv2
import numpy as np
#from numpy.lib.utils import source
from skimage import io
import card_transformation as ct

imported_image = io.imread("./img/cards.jpg")
imported_image = cv2.cvtColor(imported_image,cv2.COLOR_BGR2RGB)

source_points = np.float32([[111,217],
        [289,184],
	[154,483],
	[355,439]])

cv2.imshow('myImage2',ct.perspective(imported_image,source_points))
cv2.waitKey(0) 
cv2.destroyAllWindows()

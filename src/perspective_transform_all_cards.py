#  Autor: Caio Maia - caiomaia3@gmail.com
#  Este script tem o objetivo de experimentar as funções básicas do open-cv
import cv2
import numpy as np
from numpy.lib.utils import source
# from numpy.lib.utils import source
from skimage import io
import card_transformation as ct

imported_image = io.imread("/home/senai/Projects/Active/desafio-visao-computacional/img/cards.jpg")
imported_image = cv2.cvtColor(imported_image,cv2.COLOR_BGR2RGB)

# cv2.imshow('myImage2',imported_image)
# cv2.waitKey(0) 
# cv2.destroyAllWindows()

# 1 ---- 2
# |	 |
# |	 |
# |	 |
# 4 ---- 3

k_spades = np.float32([[111,217],
        [289,184],
	[154,483],
	[355,439]])

k_dimonds = np.float32([[273,116],
	     [453,129],
	     [273,362],
	     [457,373]])

# k_dimonds_top_line = [[276,116],[453,126]]
# k_dimonds_mid_point = ct.line_mid_point(k_dimonds_top_line)
# print(k_dimonds_mid_point)

lineColor = [255,255,0] #Blue
circleRadius = 2
lineWidth = 5

# cv2.circle(imported_image,k_dimonds_mid_point,circleRadius,lineColor,lineWidth) # Vértice 1




# k_dimonds = np.float32([[276,116],
#         [453,126],
# 	[154,483],
# 	[355,439]])
source_points = k_dimonds
base_image = ct.perspective(imported_image,source_points)

mask = np.zeros(base_image.shape[:2], dtype="uint8")
triangle = np.array([[0,0],
	     [250,0],
	     [250,350]],np.int32)


cv2.drawContours(mask,[triangle],0,255,-1)
masked = cv2.bitwise_and(base_image,base_image,mask=mask)
masked_flipped = cv2.flip(masked,-1)
final_image = cv2.add(masked,masked_flipped)
cv2.imshow('myImage2',final_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()

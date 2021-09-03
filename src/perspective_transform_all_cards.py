#  Autor: Caio Maia - caiomaia3@gmail.com
#  Este script tem o objetivo de resolver um desafio proposto no Centro de Competência em Robótica e Sistemas Autônomos do SENAI
import cv2
import numpy as np
from numpy.lib.utils import source
# from numpy.lib.utils import source
from skimage import io
import card_transformation as ct

imported_image = io.imread("./img/cards.jpg")
imported_image = cv2.cvtColor(imported_image,cv2.COLOR_BGR2RGB)

# 1 ---- 2
# |	 |
# |	 |
# |	 |
# 3 ---- 4

## K-Spades
k_spades_points = np.float32([[111,217],
        [289,184],
	[154,483],
	[355,439]])

image_name = 'K-Spades'
k_spades_image = ct.perspective(imported_image,k_spades_points)
ct.show_image(image_name,k_spades_image)


## K-Dimonds
k_dimonds_points = np.float32([[275,116],
	     [453,127],
	     [259,366],
	     [457,373]])

source_points = k_dimonds_points
base_image = ct.perspective(imported_image,source_points)
ct.show_image(image_name,base_image)

## Use flipped_image to repompose the K Dimonds Card.
flipped_image = base_image 
flipped_image = cv2.flip(flipped_image,-1)


## Define ROI (Region of Interest)
mask = np.zeros(base_image.shape[:2], dtype="uint8")
crop_contour = np.array([[94,350],
	     [0,350],
	     [0,100],
	     [25,100]],np.int32)
cv2.drawContours(mask,[crop_contour],0,255,-1)
ct.show_image(image_name,mask)
inverse_mask = cv2.bitwise_not(mask)
image_cropped_1 = cv2.bitwise_and(base_image,base_image,mask=inverse_mask)
image_cropped_2 = cv2.bitwise_and(flipped_image,flipped_image,mask=mask)

k_dimonds_image = cv2.add(image_cropped_1,image_cropped_2)
image_name = "K-Dimonds"

ct.show_image(image_name,k_dimonds_image)
#  Autor: Caio Maia - caiomaia3@gmail.com
#  Este script tem o objetivo de experimentar as funções básicas do open-cv
import cv2
import numpy as np
from numpy.lib.utils import source
from skimage import io

##Import image
imported_image = io.imread("/home/senai/Projects/Active/desafio-visao-computacional/img/cards.jpg")
test_image = io.imread("/home/senai/Projects/Active/desafio-visao-computacional/img/cards.jpg")
test_image = cv2.cvtColor(test_image,cv2.COLOR_BGR2RGB)
imported_image = cv2.cvtColor(imported_image,cv2.COLOR_BGR2RGB)

## Mark points
vertices = [[111,217],
        [289,184],
	[154,483],
	[355,439]]

lineColor = [255,255,0] #Blue
circleRadius = 2
lineWidth = 5

for point in vertices:
	cv2.circle(test_image,point,circleRadius,lineColor,lineWidth) # Vértice 1


##Vertices visualization
cv2.imshow('myImage',test_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()


## Define card size and position
card_height = 350
card_width  = 250

#Print card location
start_point = [0,0]
end_point   =[card_width,card_height]
rectangle_color = [0,0,255]

cv2.rectangle(test_image,start_point,end_point,rectangle_color,lineWidth)
cv2.imshow('myImage',test_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()

## Image transformation

source_points = np.float32(vertices)
destination_points = np.float32([start_point,
				[start_point[0]+card_width, start_point[1]],
				[start_point[0], start_point[1]+card_height],
				end_point])

transformation_matrix = cv2.getPerspectiveTransform(source_points,destination_points)

output_image = cv2.warpPerspective(imported_image,transformation_matrix,(card_width,card_height))

cv2.imshow('myImage2',output_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()


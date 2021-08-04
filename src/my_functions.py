
import cv2
import numpy as np

def foo():
	print("Olá")
	
def card_trasnform(input_image,source_points):
	## Define card size and position
	card_height = 350
	card_width  = 250

	start_point = [0,0]
	end_point   =[card_width,card_height]
	destination_points = np.float32([start_point,
				[card_width,0],
				[0,card_height],
				end_point])
				
	transformation_matrix = cv2.getPerspectiveTransform(source_points,destination_points)
	output_image = cv2.warpPerspective(input_image,transformation_matrix,(card_width,card_height))
	return output_image


import cv2
import numpy as np

def foo():
	print("Olá")
	
def perspective(input_image,source_points):
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


def line_mid_point(points):
	pt0 = np.float32(points[0])
	pt1 = np.float32(points[1])
	pt_mid_float = ((pt0+pt1)/2)
	pt_mid = pt_mid_float.astype(int)
	return pt_mid.tolist()

def show_image(image_name,image):
	cv2.imshow(image_name,image)
	cv2.waitKey(0) 
	cv2.destroyAllWindows()

def create_new_mask(base_image,contour):
	mask = np.zeros(base_image.shape[:2], dtype="uint8")
	cv2.drawContours(mask,[contour],0,255,-1)
	return mask

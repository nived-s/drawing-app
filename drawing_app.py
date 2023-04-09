import cv2
import numpy as np


# A matrix of 600 and 600 is created with value default as 1
# multiplied by 255 to get white bg color value
# color channels = 3
canvas = np.ones([600,600,3], 'uint8')*255

color = (0, 255,0)

# set to True when mouse clicked and drawing begins
draw_mode = False

# starting coordinates for mouse pointer 
#activated only when mouse clicked
start_point_x, start_point_y = None, None

# click callback function
def click(event, end_point_x, end_point_y, flags, param):
	global canvas, start_point_x, start_point_y, draw_mode

	# button down starts capturing mouse coordinates to pass to line()
	if event == cv2.EVENT_LBUTTONDOWN:
		draw_mode = True				# mouse clicked changing draw mode to True for drawing
		start_point_x = end_point_x
		start_point_y = end_point_y 
		
		
	elif event == cv2.EVENT_MOUSEMOVE:
		# cv2.line(image, start_point, end_point, color, thickness)
		if draw_mode == True:
			cv2.line(canvas, (start_point_x, start_point_y), (end_point_x, end_point_y), color, thickness = 3)

			# updating starting and ending point infinitely unless mouse btn up
			start_point_x, start_point_y = end_point_x, end_point_y
		

	elif event == cv2.EVENT_LBUTTONUP:
		# mouse btn released drawing mode is changed to default 
		draw_mode = False


# window creation and callback function
cv2.namedWindow("Drawing window")
cv2.setMouseCallback("Drawing window", click)


while True:
	cv2.imshow("Drawing window", canvas)

	# checking for 'q' to pressed every 1 ms to close the window
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break
import cv2
import numpy as np
capture = cv2.VideoCapture('coringa.mp4')
length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

size = (
	int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
	int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
)

codec = cv2.VideoWriter_fourcc(*'DIVX')
output = cv2.VideoWriter('mediana.avi', codec, 23.0, size)

while(True):
	ret, frame = capture.read()
	if frame is None:
		break

	frame = np.vstack([
	 np.hstack([frame,
	 cv2.medianBlur(frame, 3)]),
	 np.hstack([cv2.medianBlur(frame, 5),
	 cv2.medianBlur(frame, 7)]),
	 np.hstack([cv2.medianBlur(frame, 9),
	 cv2.medianBlur(frame, 11)]),
	 ])
	 
	output.write(frame)

capture.release()
cv2.destroyAllWindows()
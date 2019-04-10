import cv2

capture = cv2.VideoCapture('coringa.mp4')
length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

size = (
  int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
  int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
)

codec = cv2.VideoWriter_fourcc(*'DIVX')
output = cv2.VideoWriter('media.avi', codec, 23.0, size)

while(True):
   ret, frame = capture.read()
   if frame is None:
     break

   frame = cv2.blur(frame, ( 7, 7))
   output.write(frame)

capture.release()
cv2.destroyAllWindows()
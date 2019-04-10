import cv2
import numpy as np

def split_video_channels():

    cap = cv2.VideoCapture('coringa.mp4')
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    size = (
      int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    )
    codec = cv2.VideoWriter_fourcc(*'DIVX')
    outputB = cv2.VideoWriter('outB.avi', codec, 23.0, size)
    outputG = cv2.VideoWriter('outG.avi', codec, 23.0, size)
    outputR = cv2.VideoWriter('outR.avi', codec, 23.0, size)
    while True:
        ret_val, frame = cap.read()
        if ret_val == True:
            height, width, _ = frame.shape
            zeroImgMatrix = np.zeros((height, width), dtype="uint8")
            (B, G, R) = cv2.split(frame)
            R = cv2.merge([zeroImgMatrix, zeroImgMatrix, R])
            G = cv2.merge([zeroImgMatrix, G, zeroImgMatrix])
            B = cv2.merge([B, zeroImgMatrix, zeroImgMatrix])
            outputR.write(R) #Salva em red
            outputG.write(G) #Salva em green
            outputB.write(B) #Salva em blue
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

split_video_channels()
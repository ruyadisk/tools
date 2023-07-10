import cv2
import datetime

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter((str(datetime.datetime.now()) + '.mp4'), cv2.VideoWriter_fourcc(*'DIVX') ,20 ,(width,height))

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("Start Recording")
        while True:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            writer.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('p'):
                print("End Recording")
                writer.release()
                cap.release()
                cv2.destroyAllWindows()
	


    
    
    
import cv2
import numpy as np

# Load the pretrained Yunet model
model_path = 'pretrained_model/face_detection_yunet_2023mar.onnx'
yunet = cv2.FaceDetectorYN.create(model_path, '', (320, 320), 0.7, 0.3, 5000)

# Yunet implementation
def detect_face_yunet(frame):
    #cap = cv2.VideoCapture(0)
    
    #while True:
        #ret, frame = cap.read()
        #if not ret:
            #break

        height, width = frame.shape[:2]
        yunet.setInputSize((width, height))

        _, face = yunet.detect(frame)

        if face is not None:
            for f in face:
                f = f.astype(np.int32)
                
                bbox = f[0:4]
                cv2.rectangle(frame, (bbox[0], bbox[1]), 
                              (bbox[0]+bbox[2], bbox[1]+bbox[3]), 
                              (0, 255, 0), 2)

                if len(f) > 4:
                    landmark = f[4:14].reshape((5, 2))
                    for (x, y) in landmark:
                        cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)
                        
        #cv2.imshow('Face Detection', frame)

        #if cv2.waitKey(1) & 0xFF == ord('q'):
            #break
            
    #cap.release()
    #cv2.destroyAllWindows()

def main():
    detect_face_yunet()

if __name__ == "__main__":
    main()
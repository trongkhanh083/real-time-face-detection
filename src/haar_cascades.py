import cv2

# Load the pretrained Haar Cascades classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Haar Cascades implementation
def detect_face_haar(frame):
    #cap = cv2.VideoCapture(0)
    
    #while True:
        #ret, frame = cap.read()
        #if not ret:
            #break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        #cv2.imshow('Face Detection', frame)
        
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            #break

    #cap.release()
    #cv2.destroyAllWindows()

def main():
    detect_face_haar()

if __name__ == "__main__":
    main()
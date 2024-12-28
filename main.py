import cv2 as cv
from fer import FER

# Initialize Webcam
capture = cv.VideoCapture(0)

# Load Haar Cascade for Face Detection
haar_cascade = cv.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

# Initialize FER for Emotion Detection
emotion_detector = FER(mtcnn=True)

while True:
    # Read Frame from Webcam
    isTrue, frame = capture.read()

    # Detect Faces
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)
    for (x, y, w, h) in faces_rect:
        # Draw Rectangle around Faces
        face_roi = frame[y:y+h, x:x+w]
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Detect Emotions
        emotion, score = emotion_detector.top_emotion(face_roi)
        if emotion:
            # Display Detected Emotion
            cv.putText(frame, f"{emotion} ({int(score * 100)}%)", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show the Frame
    cv.imshow("Video", frame)

    # Break on 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release Resources
capture.release()
cv.destroyAllWindows()

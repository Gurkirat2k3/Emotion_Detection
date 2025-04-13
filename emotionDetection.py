import cv2
from fer import FER

# Initialize the emotion detector
detector = FER()

# Load the pre-trained face detection model from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

frame_count = 0  # Counter for frame skipping

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture frame")
        break

    # Resize frame for faster processing (reduce computational load)
    frame = cv2.resize(frame, (640, 480))  

    # Convert frame to grayscale (for face detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Process every 3rd frame to improve performance
    if frame_count % 3 == 0:
        # Detect faces using OpenCV's Haarcascade
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Store detected emotions
        emotions = detector.detect_emotions(frame)

    # Draw rectangles and labels for detected faces and their emotions
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Find the emotion corresponding to the detected face
        for emotion in emotions:
            (ex, ey, ew, eh) = emotion["box"]
            
            # Ensure the detected face matches the detected emotion
            if abs(x - ex) < 20 and abs(y - ey) < 20:
                dominant_emotion = max(emotion["emotions"], key=emotion["emotions"].get)
                
                # Display the detected emotion
                cv2.putText(frame, dominant_emotion, (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                break  # Prevent duplicate emotions for a single face

    # Display the processed frame
    cv2.imshow('Optimized Emotion Detection', frame)

    # Increment frame counter
    frame_count += 1

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

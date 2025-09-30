import cv2
import mediapipe as mp

# Initialize Mediapipe Face Detection
mp_face_detection = mp.solutions.face_dvetection
mp_drawing = mp.solutions.drawing_utils

# Use the default webcam (0)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Start the face detection process
with mp_face_detection.FaceDetection(
    min_detection_confidence=0.5) as face_detection:
    
    # Loop to continuously read frames from the webcam
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Ignoring empty camera frame.")
            continue

        # Flip the frame horizontally for a more natural view
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and find faces
        results = face_detection.process(rgb_frame)

        # If faces are detected, draw the bounding boxes
        if results.detections:
            for detection in results.detections:
                # Get the bounding box coordinates
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                            int(bboxC.width * iw), int(bboxC.height * ih)

                # Draw the rectangle around the face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # Optional: Display confidence score
                score = detection.score[0]
                cv2.putText(frame, f'Face: {int(score * 100)}%', (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the output frame
        cv2.imshow('Real-Time Face Detection', frame)
        
        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
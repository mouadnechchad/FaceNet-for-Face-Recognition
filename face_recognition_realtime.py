import cv2
import numpy as np
import joblib
from keras_facenet import FaceNet

# Load the logistic regression model
model_filename = 'face_recognition.pkl'
loaded_model = joblib.load(model_filename)

# Initialize FaceNet for generating face embeddings
embedder = FaceNet()

# Open a connection to the camera
cap = cv2.VideoCapture(0)  # Use camera index 0 (default camera)

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    if not ret:
        print("Error: Could not read a frame from the camera.")
        break

    # Preprocess the frame (resize to the same shape as your training data)
    frame = cv2.resize(frame, (160, 160))

    # Generate embeddings for the frame
    embedding = embedder.embeddings(np.array([frame]))

    # Use the loaded logistic regression model to make predictions
    predicted_label = loaded_model.predict(embedding)

    # Display the prediction on the frame
    label_text = f"Label: {predicted_label[0]}"
    print(label_text)
    cv2.putText(frame, label_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame with predictions using OpenCV
    cv2.imshow('Real-time Prediction', frame)

    # Exit the loop if you want to stop capturing frames
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close the OpenCV windows

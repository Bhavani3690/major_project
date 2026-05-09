import cv2
import numpy as np
from tensorflow.keras.models import load_model

print("Loading model...")
model = load_model("model.h5")
print("Model loaded successfully!")

labels = ["Hello", "Yes", "Thank You"]

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not working. Trying alternate camera...")
    cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("No camera found ❌")
    exit()

print("Webcam started!")
print("Press SPACE to predict")
print("Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    cv2.imshow("Sign Language Detection", frame)

    key = cv2.waitKey(1)

    if key == 32:  # SPACE
        img = cv2.resize(frame, (64, 64))
        img = np.reshape(img, (1, 64, 64, 3))

        prediction = model.predict(img, verbose=0)
        label = labels[np.argmax(prediction)]

        print("Predicted:", label)

        cv2.putText(frame, label, (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.imshow("Prediction", frame)
        cv2.waitKey(1500)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
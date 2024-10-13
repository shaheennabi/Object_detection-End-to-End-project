import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"

labels =['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']
number_of_images = 500

for label in labels:
    image_path = os.path.join(IMAGE_PATH, label)
    
    # Create directory if it doesn't exist
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    # Open the camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        break
    
    print(f"Collecting images for {label}")
    time.sleep(3)

    # Wait for a key press to proceed
    print("Press any key to start collecting images for this label...")
    cv2.waitKey(0)  # Wait indefinitely for a key press

    # After key press, wait for 5 seconds to prepare
    print(f"Starting in 5 seconds for label {label}...")
    time.sleep(5)

    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to capture image.")
            break

        # Add label and image number text on the frame
        text = f'Label: {label}, Image: {imgnum + 1}/{number_of_images}'
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Save the image
        imagename = os.path.join(IMAGE_PATH, label, f'{label}.{str(uuid.uuid1())}.jpg')
        cv2.imwrite(imagename, frame)

        # Display the frame
        cv2.imshow('frame', frame)

        # Check if any key is pressed
        key = cv2.waitKey(1) & 0xFF
        
        # Press 'q' to quit
        if key == ord('q'):
            break
        
        # Press spacebar (' ') to pause for 5 seconds
        elif key == ord(' '):
            print("Pausing for 5 seconds to change background...")
            time.sleep(5)
            print("Resuming capture...")

        # Optional: Adjust the sleep time for delays between captures
        time.sleep(1)

    cap.release()

# Ensure OpenCV windows are closed properly
cv2.destroyAllWindows()

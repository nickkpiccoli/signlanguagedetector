import cv2
from CapturedHand import CapturedHand
import numpy as np

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    tracker = CapturedHand()

    # For webcam input:
    with tracker.mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5, static_image_mode=False) as hands:

      while cap.isOpened():
        success, image = cap.read()
        if not success:
          print("Ignoring empty camera frame.")
          # If loading a video, use 'break' instead of 'continue'.
          continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        tracker.draw_landmark(image,results)

        #collecting x,y,z landmarks lists for

        x = np.array(tracker.get_x_landmarks(results))
        y = np.array(tracker.get_y_landmarks(results))
        z = np.array(tracker.get_z_landmarks(results))

        if(x.shape != (0,)):
          print(x[0,8])

        # Flip the image horizontally for a selfie-view display and show image.
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
          break
    cap.release()

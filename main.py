import cv2
import mediapipe as mp

class CapturedHand:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands

    def draw_landmark(self,results):
        if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
            self.mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                self.mp_hands.HAND_CONNECTIONS,
                self.mp_drawing_styles.get_default_hand_landmarks_style(),
                self.mp_drawing_styles.get_default_hand_connections_style())

    ##TODO each function return a list of 21 landmarks of x,y,x axis

    def get_x_landmarks(self, results):
        landmarks = []
        #checking if landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(21):
                    landmarks.append(hand_landmarks.landmark[i].x)
        else:
            return landmarks

        return landmarks

    def get_y_landmarks(self, results):
        landmarks = []
        # checking if landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(21):
                    landmarks.append(hand_landmarks.landmark[i].y)
        else:
            return landmarks

        return landmarks

    def get_z_landmarks(self, results):
        landmarks = []
        # checking if landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(21):
                    landmarks.append(hand_landmarks.landmark[i].z)
        else:
            return landmarks

        return landmarks

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

        tracker.draw_landmark(results)

        #collecting x,y,z landmarks lists

        # Flip the image horizontally for a selfie-view display and show image.
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
          break
    cap.release()

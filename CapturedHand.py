import mediapipe as mp


class CapturedHand:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands

    def draw_landmark(self, image, results):
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
        # checking if landmarks are detected
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

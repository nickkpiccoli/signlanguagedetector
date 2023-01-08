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

    def classificate_hand(self,results):
        if results.multi_hand_landmarks:
            hands=[]
            if len(results.multi_handedness) == 2:
                hands.append((results.multi_handedness[0].classification[0].index,
                             results.multi_handedness[0].classification[0].label))
                hands.append((results.multi_handedness[1].classification[0].index,
                             results.multi_handedness[1].classification[0].label))
            else:
                hands.append((results.multi_handedness[0].classification[0].index,
                              results.multi_handedness[0].classification[0].label))
        return hands

    #TODO verify that works also like this
    def draw_3d_world(self,results):
        # Draw hand world landmarks.
        if not results.multi_hand_world_landmarks:
            pass
        for hand_world_landmarks in results.multi_hand_world_landmarks:
            self.mp_drawing.plot_landmarks(
                hand_world_landmarks, self.mp_hands.HAND_CONNECTIONS, azimuth=5)

    ##TODO each function return a list of 21 landmarks of x,y,x axis
    def get_x_landmarks(self, results):
        landmarks = []
        # checking if landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                single_hand = []
                for i in range(21):
                    single_hand.append(hand_landmarks.landmark[i].x)
                landmarks.append(single_hand)
        return landmarks

    def get_y_landmarks(self, results):
        landmarks = []
        # checking if landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                single_hand = []
                for i in range(21):
                    single_hand.append(hand_landmarks.landmark[i].y)
                landmarks.append(single_hand)
        return landmarks

    def get_z_landmarks(self, results):
        landmarks = []
        # checking if landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                single_hand = []
                for i in range(21):
                    single_hand.append(hand_landmarks.landmark[i].z)
                landmarks.append(single_hand)
        return landmarks

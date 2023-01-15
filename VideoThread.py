from PyQt5.QtGui import *
from PyQt5.QtCore import *

from CapturedHand import CapturedHand
import numpy as np
import cv2

class VideoThread(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True

        tracker = CapturedHand()
        cap = cv2.VideoCapture(0)
        with tracker.mp_hands.Hands(
                model_complexity=0,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5, static_image_mode=False) as hands:

            while self.ThreadActive:
                ret, frame = cap.read()
                if ret:
                    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    FlippedImage = cv2.flip(Image, 1)

                    results = hands.process(FlippedImage)
                    FlippedImage = cv2.cvtColor(FlippedImage, cv2.COLOR_RGB2BGR)
                    tracker.draw_landmark(FlippedImage, results)

                    FlippedImage = cv2.cvtColor(FlippedImage, cv2.COLOR_BGR2RGB)

                    x = np.array(tracker.get_x_landmarks(results))
                    y = np.array(tracker.get_y_landmarks(results))
                    z = np.array(tracker.get_z_landmarks(results))

                    if (x.shape != (0,)):
                        print(x[0, 8])

                    ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(700, 700, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(Pic)

        cap.release()


    def stop(self):
        self.ThreadActive = False
        self.quit()
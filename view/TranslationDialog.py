from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from VideoThread import VideoThread


class TranslationDialog(QWidget):
    def __init__(self):
        super(TranslationDialog, self).__init__()
        self.setGeometry(600, 600, 900, 900)

        self.main_layout = QHBoxLayout()
        self.camera_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.camera_layout.addWidget(self.FeedLabel)

        self.CameraButton = QPushButton("Start Camera")
        self.CameraButton.clicked.connect(self.camera_feed)

        self.RecordButton = QPushButton("Start Recording")
        self.RecordButton.clicked.connect(self.record_data)

        self.right_layout.addWidget(self.CameraButton)
        self.right_layout.addWidget(self.RecordButton)

        self.Worker1 = VideoThread()

        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

        self.main_layout.addLayout(self.camera_layout)
        self.main_layout.addLayout(self.right_layout)
        self.setLayout(self.main_layout)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def camera_feed(self):
        if self.CameraButton.text() == 'Start Camera':
            self.Worker1.start()
            self.CameraButton.setText('Stop Camera')
        else:
            self.Worker1.stop()
            self.CameraButton.setText('Start Camera')

    def record_data(self):
        pass

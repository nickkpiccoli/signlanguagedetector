from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from view.TranslationDialog import TranslationDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.translation = TranslationDialog()
        self.setCentralWidget(self.translation)
        self.create_menubar()

    def create_menubar(self):
        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('File')
        editMenu = self.menubar.addMenu('Edit')


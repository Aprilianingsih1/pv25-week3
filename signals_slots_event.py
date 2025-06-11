import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import (QWidget, QSlider, QVBoxLayout, QApplication, QLCDNumber, QMainWindow)

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example (QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Exit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

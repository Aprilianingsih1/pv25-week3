import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QSlider, QVBoxLayout, QApplication, QLCDNumber)



class Example (QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        lcd = QLCDNumber(self)

        sld = QSlider(Qt.Horizontal, self)
        sld.valueChanged.connect(lcd.display)
        sld.setMinimum(1)
        sld.setMaximum(50)
        sld.setTickInterval(10)
        sld.setTickPosition(QSlider.TicksAbove)

        vbox =QVBoxLayout()
        vbox.addWidget(sld)
        vbox.addWidget(lcd)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from My_Custom_Widgets import CustomQCalendarWidget


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(500, 500)

        # CREATE CONTAINER AND LAYOUT
        self.container = QFrame()
        self.container.setObjectName('container')
        self.container.setStyleSheet('#container { background-color: #222 }')
        self.layout = QVBoxLayout()

        # ADD WIDGETS TO LAYOUT
        self.toggle = CustomQCalendarWidget()
        self.layout.addWidget(self.toggle, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)

        # SET CENTRAL WIDGET
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # SHOW WINDOW
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = MainWindow()
    sys.exit(app.exec())
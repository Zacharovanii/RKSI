from design import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QPropertyAnimation


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Long_slider.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.Change_long_btn.clicked.connect(self.hide_slider)
        self.ui.frame.change_func(self.show_slider)

        # animations
        self.frame_animation_show = QPropertyAnimation(self.ui.Long_slider, b'geometry')
        self.frame_animation_show.setDuration(500)

        self.frame_animation_hide = QPropertyAnimation(self.ui.Long_slider, b'geometry')
        self.frame_animation_hide.setDuration(500)
        self.frame_animation_hide.finished.connect(self.hide_slider)

    def hide_slider(self):
        if isinstance(self.sender(), QPropertyAnimation):
            self.ui.Long_slider.hide()
            self.ui.frame.show()
        else:
            self.frame_animation_hide.setStartValue(self.ui.Long_slider.geometry())
            self.frame_animation_hide.setEndValue(self.ui.frame.geometry())
            self.frame_animation_hide.start()

    def show_slider(self):
        print('c')
        self.ui.frame.hide()
        self.ui.Long_slider.show()

        self.frame_animation_show.setStartValue(self.ui.frame.geometry())
        self.frame_animation_show.setEndValue(self.ui.Long_slider.geometry())
        self.frame_animation_show.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


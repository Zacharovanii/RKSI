from design import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QPropertyAnimation, Qt, QSize, QParallelAnimationGroup, QRect
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.slider_b.hide()
        self.ui.stackedWidget.setCurrentIndex(0)

        # Slider click action
        # self.ui.slider_m.change_func(self.show_slider)
        # self.ui.slider_b.change_func(self.hide_slider)

        # Main Window customization
        self.setWindowTitle('RKSI schedule')
        # self.setWindowFlag()

        self.ui.statusbar.setVisible(False)
        self.ui.menubar.setVisible(False)

        icon_sizes = (30, 30)
        self.ui.btn_sm_schedule.setIcon(QIcon('icons/schedule.svg'))
        self.ui.btn_sb_schedule.setIcon(QIcon('icons/schedule.svg'))
        self.ui.btn_sm_schedule.setIconSize(QSize(*icon_sizes))
        self.ui.btn_sb_schedule.setIconSize(QSize(*icon_sizes))
        self.ui.btn_sm_marks.setIcon(QIcon('icons/marks.svg'))
        self.ui.btn_sb_marks.setIcon(QIcon('icons/marks.svg'))
        self.ui.btn_sm_marks.setIconSize(QSize(*icon_sizes))
        self.ui.btn_sb_marks.setIconSize(QSize(*icon_sizes))
        self.ui.btn_sm_settings.setIcon(QIcon('icons/settings.svg'))
        self.ui.btn_sb_settings.setIcon(QIcon('icons/settings.svg'))
        self.ui.btn_sm_settings.setIconSize(QSize(*icon_sizes))
        self.ui.btn_sb_settings.setIconSize(QSize(*icon_sizes))
        self.ui.btn_sm_move.setIcon(QIcon('icons/move_menu.svg'))
        self.ui.btn_sb_move.setIcon(QIcon('icons/move_menu.svg'))
        self.ui.btn_sm_move.setIconSize(QSize(*icon_sizes))
        self.ui.btn_sb_move.setIconSize(QSize(*icon_sizes))

        self.setStyleSheet('''
        QMainWindow {
            background-color: #333333;
        }
        
        QPushButton {
            background-color: #333333;
            color: white;
            border: none;
            padding: 10px;
        }
        
        QPushButton:hover {
            background-color: #5E81AC;
        }
        
        QLabel {
            color: white;
            background-color: #2E3440;  
            padding: 10px;  
            font-size: 20px;  
            font-weight: bold;  

        }
        ''')

        self.ui.calendar.setStyleSheet('''
        QCalendarWidget {
            border-radius: 5px;
            border: 1px solid #dcdcdc;
        }
        QCalendarWidget QToolButton {
            color: white;
            background-color: #282828;
            border: none;
            border-radius: 5px;
            padding: 5px;
            margin: 5px;
        }
        
        QCalendarWidget QToolButton:hover {
            background-color: #666666;
        }
        
        QCalendarWidget QWidget#qt_calendar_navigationbar {
            background-color: #282828;
            border-radius: 10px;
        }
        
        QCalendarWidget QMenu {
            background-color: #282828;
            color: white;
        }
        
        QCalendarWidget QSpinBox {
            background-color: #2c3e50;
            color: white;
            border: none;
        }
        
        #qt_calendar_prevmonth {
            icon-size: 25px;
            qproperty-icon: url(icons/left_arrow.png);
        }
        
        #qt_calendar_nextmonth {
            icon-size: 25px;
            qproperty-icon: url(icons/right_arrow.png);
        }
        
        QCalendarWidget QAbstractItemView:enabled {
            background-color: #2c3e50;
            color: white;
        } 
        
        QCalendarWidget QAbstractItemView:disabled {
            background-color: #2c3e50;
            color: rgba(51, 51, 51, 0.7);;
        }
        ''')

        self.ui.slider_m.setStyleSheet('''
        QFrame {
            background-color:  #002F55;
        }
        
        QPushButton {
            background-color: #002F55;
            color: white;
            border: none;
            padding: 10px;
        }
        
        QPushButton:hover {
            background-color: #5E81AC;
        }
        ''')
        self.ui.slider_b.setStyleSheet('''
        QFrame {
            background-color:  #002F55;
        }
        QPushButton {
            background-color: #002F55;
            color: white;
            border: none;
            padding: 10px;
        }
        
        QPushButton:hover {
            background-color: #5E81AC;
        }
        ''')

        # Frame buttons
        self.ui.btn_sm_move.clicked.connect(self.show_slider)
        self.ui.btn_sb_move.clicked.connect(self.hide_slider)

        self.ui.btn_sm_schedule.clicked.connect(self.moveToSchedule)
        self.ui.btn_sb_schedule.clicked.connect(self.moveToSchedule)

        self.ui.btn_sm_marks.clicked.connect(self.moveToMarks)
        self.ui.btn_sb_marks.clicked.connect(self.moveToMarks)

        self.ui.btn_sm_settings.clicked.connect(self.moveToSettings)
        self.ui.btn_sb_settings.clicked.connect(self.moveToSettings)

        # animations
        self.frame_animation_show = QPropertyAnimation(self.ui.slider_b, b'geometry')
        self.frame_animation_show.setDuration(125)

        self.frame_animation_hide = QPropertyAnimation(self.ui.slider_b, b'geometry')
        self.frame_animation_hide.setDuration(125)

        self.stackedWidget_animation = QPropertyAnimation(self.ui.stackedWidget, b'geometry')
        self.stackedWidget_animation.setDuration(125)

    def moveToSchedule(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def moveToMarks(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def moveToSettings(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def hide_slider(self):
        if isinstance(self.sender(), QParallelAnimationGroup):
            self.ui.slider_b.hide()
            self.ui.slider_m.show()
        else:
            slider_b_geometry = self.ui.slider_b.geometry()
            slider_m_geometry = self.ui.slider_m.geometry()

            stacked_widget_animation_start_value = self.ui.stackedWidget.geometry()
            stacked_widget_animation_end_value = slider_m_geometry.united(stacked_widget_animation_start_value)

            self.frame_animation_hide.setStartValue(slider_b_geometry)
            self.frame_animation_hide.setEndValue(slider_m_geometry)
            self.stackedWidget_animation.setStartValue(stacked_widget_animation_start_value)
            self.stackedWidget_animation.setEndValue(stacked_widget_animation_end_value)

            group_animation = QParallelAnimationGroup(self)
            group_animation.addAnimation(self.stackedWidget_animation)
            group_animation.addAnimation(self.frame_animation_hide)
            group_animation.start()
            group_animation.finished.connect(self.hide_slider)

    def show_slider(self):
        self.stackedWidget_animation.setStartValue(self.ui.stackedWidget.geometry())
        self.ui.slider_m.hide()
        self.ui.slider_b.show()
        self.stackedWidget_animation.setEndValue(self.ui.stackedWidget.geometry())

        self.frame_animation_show.setStartValue(self.ui.slider_m.geometry())
        self.frame_animation_show.setEndValue(self.ui.slider_b.geometry())

        group_animation = QParallelAnimationGroup(self)
        group_animation.addAnimation(self.stackedWidget_animation)
        group_animation.addAnimation(self.frame_animation_show)
        group_animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


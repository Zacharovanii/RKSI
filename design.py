# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)
from py_toggle import CQFrame

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = CQFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(60, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Slider = QVBoxLayout()
        self.Slider.setSpacing(0)
        self.Slider.setObjectName(u"Slider")
        self.Slider.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Slider_name = QLabel(self.frame)
        self.Slider_name.setObjectName(u"Slider_name")

        self.horizontalLayout.addWidget(self.Slider_name)

        self.Change_btn = QPushButton(self.frame)
        self.Change_btn.setObjectName(u"Change_btn")

        self.horizontalLayout.addWidget(self.Change_btn)


        self.Slider.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.Slider_btn_to_schedule = QPushButton(self.frame)
        self.Slider_btn_to_schedule.setObjectName(u"Slider_btn_to_schedule")
        self.Slider_btn_to_schedule.setMaximumSize(QSize(50, 50))
        self.Slider_btn_to_schedule.setBaseSize(QSize(50, 0))

        self.verticalLayout.addWidget(self.Slider_btn_to_schedule)

        self.Slider_btn_to_marks = QPushButton(self.frame)
        self.Slider_btn_to_marks.setObjectName(u"Slider_btn_to_marks")
        self.Slider_btn_to_marks.setMaximumSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.Slider_btn_to_marks)


        self.Slider.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(109, 129, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Slider.addItem(self.verticalSpacer)

        self.Slider_btn_settings = QPushButton(self.frame)
        self.Slider_btn_settings.setObjectName(u"Slider_btn_settings")

        self.Slider.addWidget(self.Slider_btn_settings)


        self.gridLayout.addLayout(self.Slider, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame)

        self.Long_slider = QFrame(self.centralwidget)
        self.Long_slider.setObjectName(u"Long_slider")
        self.Long_slider.setFrameShape(QFrame.Shape.StyledPanel)
        self.Long_slider.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.Long_slider)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Slider_long = QVBoxLayout()
        self.Slider_long.setObjectName(u"Slider_long")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Slider_long_name = QLabel(self.Long_slider)
        self.Slider_long_name.setObjectName(u"Slider_long_name")

        self.horizontalLayout_2.addWidget(self.Slider_long_name)

        self.Change_long_btn = QPushButton(self.Long_slider)
        self.Change_long_btn.setObjectName(u"Change_long_btn")

        self.horizontalLayout_2.addWidget(self.Change_long_btn)


        self.Slider_long.addLayout(self.horizontalLayout_2)

        self.Slider_long_btn_to_schedule = QPushButton(self.Long_slider)
        self.Slider_long_btn_to_schedule.setObjectName(u"Slider_long_btn_to_schedule")

        self.Slider_long.addWidget(self.Slider_long_btn_to_schedule)

        self.Slider_btn_to_marks_2 = QPushButton(self.Long_slider)
        self.Slider_btn_to_marks_2.setObjectName(u"Slider_btn_to_marks_2")

        self.Slider_long.addWidget(self.Slider_btn_to_marks_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Slider_long.addItem(self.verticalSpacer_2)

        self.Slider_long_btn_settings = QPushButton(self.Long_slider)
        self.Slider_long_btn_settings.setObjectName(u"Slider_long_btn_settings")

        self.Slider_long.addWidget(self.Slider_long_btn_settings)


        self.gridLayout_2.addLayout(self.Slider_long, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.Long_slider)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 230, 47, 13))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 240, 47, 13))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 240, 49, 16))
        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Slider_name.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.Change_btn.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.Slider_btn_to_schedule.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Slider_btn_to_marks.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Slider_btn_settings.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.Slider_long_name.setText(QCoreApplication.translate("MainWindow", u"Slider_long", None))
        self.Change_long_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Slider_long_btn_to_schedule.setText("")
        self.Slider_btn_to_marks_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Slider_long_btn_settings.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Label 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Label 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi


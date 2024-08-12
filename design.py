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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QListView,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slider_m = QFrame(self.centralwidget)
        self.slider_m.setObjectName(u"slider_m")
        self.slider_m.setMaximumSize(QSize(80, 16777215))
        self.slider_m.setFrameShape(QFrame.Shape.StyledPanel)
        self.slider_m.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.slider_m)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.slider_layout = QVBoxLayout()
        self.slider_layout.setSpacing(0)
        self.slider_layout.setObjectName(u"slider_layout")
        self.slider_layout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.slider_layout.setContentsMargins(-1, 15, -1, 15)
        self.btn_sm_move = QPushButton(self.slider_m)
        self.btn_sm_move.setObjectName(u"btn_sm_move")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sm_move.sizePolicy().hasHeightForWidth())
        self.btn_sm_move.setSizePolicy(sizePolicy)
        self.btn_sm_move.setMinimumSize(QSize(45, 45))
        self.btn_sm_move.setMaximumSize(QSize(1000, 45))
        self.btn_sm_move.setBaseSize(QSize(45, 45))

        self.slider_layout.addWidget(self.btn_sm_move)

        self.btn_sm_schedule = QPushButton(self.slider_m)
        self.btn_sm_schedule.setObjectName(u"btn_sm_schedule")
        self.btn_sm_schedule.setMinimumSize(QSize(45, 45))
        self.btn_sm_schedule.setMaximumSize(QSize(1000, 45))
        self.btn_sm_schedule.setBaseSize(QSize(50, 0))
        self.btn_sm_schedule.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.slider_layout.addWidget(self.btn_sm_schedule)

        self.btn_sm_marks = QPushButton(self.slider_m)
        self.btn_sm_marks.setObjectName(u"btn_sm_marks")
        self.btn_sm_marks.setMinimumSize(QSize(45, 45))
        self.btn_sm_marks.setMaximumSize(QSize(1000, 45))

        self.slider_layout.addWidget(self.btn_sm_marks)

        self.verticalSpacer = QSpacerItem(109, 129, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.slider_layout.addItem(self.verticalSpacer)

        self.btn_sm_settings = QPushButton(self.slider_m)
        self.btn_sm_settings.setObjectName(u"btn_sm_settings")
        self.btn_sm_settings.setMinimumSize(QSize(45, 45))
        self.btn_sm_settings.setMaximumSize(QSize(1000, 45))

        self.slider_layout.addWidget(self.btn_sm_settings)


        self.gridLayout.addLayout(self.slider_layout, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.slider_m)

        self.slider_b = QFrame(self.centralwidget)
        self.slider_b.setObjectName(u"slider_b")
        self.slider_b.setFrameShape(QFrame.Shape.StyledPanel)
        self.slider_b.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.slider_b)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Slider_long = QVBoxLayout()
        self.Slider_long.setSpacing(0)
        self.Slider_long.setObjectName(u"Slider_long")
        self.Slider_long.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_sb_move = QPushButton(self.slider_b)
        self.btn_sb_move.setObjectName(u"btn_sb_move")
        self.btn_sb_move.setMinimumSize(QSize(45, 45))
        self.btn_sb_move.setMaximumSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.btn_sb_move)

        self.name_sb = QLabel(self.slider_b)
        self.name_sb.setObjectName(u"name_sb")

        self.horizontalLayout_2.addWidget(self.name_sb)


        self.Slider_long.addLayout(self.horizontalLayout_2)

        self.btn_sb_schedule = QPushButton(self.slider_b)
        self.btn_sb_schedule.setObjectName(u"btn_sb_schedule")
        self.btn_sb_schedule.setMinimumSize(QSize(0, 45))
        self.btn_sb_schedule.setMaximumSize(QSize(16777215, 45))

        self.Slider_long.addWidget(self.btn_sb_schedule)

        self.btn_sb_marks = QPushButton(self.slider_b)
        self.btn_sb_marks.setObjectName(u"btn_sb_marks")
        self.btn_sb_marks.setMinimumSize(QSize(0, 45))
        self.btn_sb_marks.setMaximumSize(QSize(16777215, 45))

        self.Slider_long.addWidget(self.btn_sb_marks)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Slider_long.addItem(self.verticalSpacer_2)

        self.btn_sb_settings = QPushButton(self.slider_b)
        self.btn_sb_settings.setObjectName(u"btn_sb_settings")
        self.btn_sb_settings.setMinimumSize(QSize(0, 45))
        self.btn_sb_settings.setMaximumSize(QSize(16777215, 45))

        self.Slider_long.addWidget(self.btn_sb_settings)


        self.gridLayout_2.addLayout(self.Slider_long, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.slider_b)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.schedule_page = QWidget()
        self.schedule_page.setObjectName(u"schedule_page")
        self.gridLayout_4 = QGridLayout(self.schedule_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.calendar = QCalendarWidget(self.schedule_page)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setGridVisible(False)
        self.calendar.setSelectionMode(QCalendarWidget.SelectionMode.SingleSelection)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)

        self.horizontalLayout_6.addWidget(self.calendar)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.group_comboBox = QComboBox(self.schedule_page)
        self.group_comboBox.setObjectName(u"group_comboBox")

        self.horizontalLayout_5.addWidget(self.group_comboBox)

        self.teacher_comboBox = QComboBox(self.schedule_page)
        self.teacher_comboBox.setObjectName(u"teacher_comboBox")

        self.horizontalLayout_5.addWidget(self.teacher_comboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.scroll_info = QScrollArea(self.schedule_page)
        self.scroll_info.setObjectName(u"scroll_info")
        self.scroll_info.setStyleSheet(u"")
        self.scroll_info.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 276, 501))
        self.scroll_info.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scroll_info)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.schedule_page)
        self.marls_page = QWidget()
        self.marls_page.setObjectName(u"marls_page")
        self.gridLayout_5 = QGridLayout(self.marls_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.marks_lable = QLabel(self.marls_page)
        self.marks_lable.setObjectName(u"marks_lable")

        self.verticalLayout_5.addWidget(self.marks_lable)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_3 = QComboBox(self.marls_page)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_4.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.marls_page)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_4.addWidget(self.comboBox_4)

        self.comboBox_5 = QComboBox(self.marls_page)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_4.addWidget(self.comboBox_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.marks_table = QTableWidget(self.marls_page)
        self.marks_table.setObjectName(u"marks_table")

        self.horizontalLayout_7.addWidget(self.marks_table)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.visit_label = QLabel(self.marls_page)
        self.visit_label.setObjectName(u"visit_label")

        self.verticalLayout_7.addWidget(self.visit_label)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.visit_graphic = QListView(self.marls_page)
        self.visit_graphic.setObjectName(u"visit_graphic")

        self.horizontalLayout_8.addWidget(self.visit_graphic)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBox_6 = QComboBox(self.marls_page)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.verticalLayout_6.addWidget(self.comboBox_6)

        self.comboBox_7 = QComboBox(self.marls_page)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.verticalLayout_6.addWidget(self.comboBox_7)

        self.comboBox_8 = QComboBox(self.marls_page)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.verticalLayout_6.addWidget(self.comboBox_8)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.gridLayout_5.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.marls_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.formLayout = QFormLayout(self.settings_page)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.settings_page)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_9.addWidget(self.label_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.settings_page)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.comboBox_9 = QComboBox(self.settings_page)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.horizontalLayout_9.addWidget(self.comboBox_9)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.settings_page)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.comboBox_10 = QComboBox(self.settings_page)
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.horizontalLayout_10.addWidget(self.comboBox_10)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.settings_page)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.checkBox = QCheckBox(self.settings_page)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_11.addWidget(self.checkBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.pushButton = QPushButton(self.settings_page)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_9.addWidget(self.pushButton)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_9)

        self.stackedWidget.addWidget(self.settings_page)

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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_sm_move.setText("")
        self.btn_sm_schedule.setText("")
        self.btn_sm_marks.setText("")
        self.btn_sm_settings.setText("")
        self.btn_sb_move.setText("")
        self.name_sb.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0432\u0438\u0433\u0430\u0446\u0438\u044f", None))
        self.btn_sb_schedule.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.btn_sb_marks.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043f\u0435\u0432\u0430\u0435\u043c\u043e\u0441\u0442\u044c", None))
        self.btn_sb_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.marks_lable.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0446\u0435\u043d\u043a\u0438", None))
        self.visit_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0435\u0449\u0430\u0435\u043c\u043e\u0441\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0438\u0442\u044c \u043e\u0431 \u043e\u0448\u0438\u0431\u043a\u0435", None))
    # retranslateUi


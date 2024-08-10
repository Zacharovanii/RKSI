from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


# from time import sleep


class PyToggle(QCheckBox):
    def __init__(
            self,
            width=60,
            bg_color='#777',
            circle_color='#DDD',
            active_color='#00BCFF',
            animation_curve=QEasingCurve.Type.OutBounce
    ):
        QCheckBox.__init__(self)

        # SET DEFAULT PARAMETERS
        self.setFixedSize(width, 28)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # COLORS
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # CREATE ANIMATION
        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b'circle_position', self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)

        # CONNECT STATE CHANGED
        self.stateChanged.connect(self.start_transition)

    @Property(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def start_transition(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(3)

        self.animation.start()
        print(f"Status: {self.isChecked()}")

    # SET NEW HIT AREA
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        p.setPen(Qt.PenStyle.NoPen)

        rect = QRect(0, 0, self.width(), self.height())

        # CHECK IF IS CHECKED
        if not self.isChecked():
            # DRAW BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)
        else:
            # DRAW BG
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)

        p.end()


class CQFrame(QFrame):
    def __init__(self, parent, func=None):
        super(CQFrame, self).__init__(parent=parent)
        self.func = func

    def event(self, e):
        if e.type() == QEvent.Type.MouseButtonPress:
            # print('clicked')
            if self.func is not None:
                self.func()

        return super().event(e)

    def change_func(self, new_func):
        self.func = new_func


class CTitleBar(QWidget):
    def __init__(self, parent=None):
        super(CTitleBar, self).__init__(parent=parent)
        self.setFixedHeight(40)

        self.close_button = QPushButton("X")
        self.minimize_button = QPushButton("-")
        self.maximize_button = QPushButton("□")

        self.setStyleSheet('''
        QWidget {
            background-color: #2E3440;        
        }
        
        QPushButton {
            background-color: #34495e;
            color: white;
            border: none;
            padding: 5px;
            font-size: 14px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #e74c3c;
        }
        ''')

        layout = QHBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(self.minimize_button)
        layout.addWidget(self.maximize_button)
        layout.addWidget(self.close_button)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.close_button.clicked.connect(parent.close)
        self.minimize_button.clicked.connect(parent.showMinimized)
        self.maximize_button.clicked.connect(parent.showMaximized)

        self.is_moving = False

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_moving = True
            self.start_point = event.pos()
            self.window_point = self.parent().frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.is_moving:
            self.parent().move(self.window_point + event.globalPosition().toPoint() - self.start_point)

    def mouseReleaseEvent(self, event):
        self.is_moving = False

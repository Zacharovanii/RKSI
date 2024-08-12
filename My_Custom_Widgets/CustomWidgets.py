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


class CustomQFrame(QFrame):
    def __init__(self, parent, func=None):
        super(CustomQFrame, self).__init__(parent=parent)
        self.func = func

    def event(self, e):
        if e.type() == QEvent.Type.MouseButtonPress:
            # print('clicked')
            if self.func is not None:
                self.func()

        return super().event(e)

    def change_func(self, new_func):
        self.func = new_func


class CustomQCalendarWidget(QCalendarWidget):
    def __init__(self, parent=None):
        super(CustomQCalendarWidget, self).__init__(parent=parent)

    def paintCell(self, painter, rect, date):
        if date == date.currentDate():
            painter.setPen(QPen(QColor(0, 200, 200), 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
            painter.drawEllipse(rect)
            # painter.drawLine(rect.topRight(), rect.topLeft())
            # painter.drawLine(rect.topRight(), rect.bottomRight())
            # painter.drawLine(rect.bottomLeft(), rect.bottomRight())
            # painter.drawLine(rect.topLeft(), rect.bottomLeft())
        super().paintCell(painter, rect, date)
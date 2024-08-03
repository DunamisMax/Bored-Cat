import math
import random
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QRadialGradient, QPainterPath
from PyQt6.QtCore import Qt, QTimer, QPointF, QLineF

class LaserPointer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Laser Pointer")
        self.setGeometry(100, 100, 800, 600)
        self.setMouseTracking(True)

        # Laser properties
        self.laser_pos = QPointF(self.width() / 2, self.height() / 2)
        self.laser_size = 10
        self.laser_color = QColor(255, 0, 0)  # Red laser
        self.trail = []
        self.trail_length = 20
        self.trail_decay = 5  # How quickly the trail fades

        # Auto-move properties
        self.auto_move = False
        self.angle = 0
        self.speed = 5

        # Set up timer for updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_laser)
        self.timer.start(16)  # ~60 FPS

    def update_laser(self):
        if self.auto_move:
            self.move_laser_auto()
        else:
            self.move_laser_to_mouse()

        self.update()  # Trigger repaint

    def move_laser_auto(self):
        # Calculate new position
        self.angle += random.uniform(-0.1, 0.1)
        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed

        # Update position
        new_x = self.laser_pos.x() + dx
        new_y = self.laser_pos.y() + dy

        # Bounce off edges
        if new_x < 0 or new_x > self.width():
            self.angle = math.pi - self.angle
        if new_y < 0 or new_y > self.height():
            self.angle = -self.angle

        # Set new position
        self.laser_pos = QPointF(
            max(0, min(new_x, self.width())),
            max(0, min(new_y, self.height()))
        )

    def move_laser_to_mouse(self):
        mouse_pos = self.mapFromGlobal(self.cursor().pos())
        self.laser_pos = QPointF(mouse_pos)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw black background
        painter.fillRect(self.rect(), Qt.GlobalColor.black)

        # Draw trail
        if len(self.trail) > 1:
            path = QPainterPath()
            path.moveTo(self.trail[0])
            for point in self.trail[1:]:
                path.lineTo(point)

            for i in range(len(self.trail) - 1):
                color = self.laser_color.lighter(100 + i * self.trail_decay)
                painter.setPen(QPen(color, 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
                painter.drawLine(QLineF(self.trail[i], self.trail[i+1]))

        # Draw laser dot
        gradient = QRadialGradient(self.laser_pos, self.laser_size)
        gradient.setColorAt(0, self.laser_color)
        gradient.setColorAt(0.8, self.laser_color.lighter(160))
        gradient.setColorAt(1, QColor(self.laser_color.red(), self.laser_color.green(), self.laser_color.blue(), 0))

        painter.setBrush(gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(self.laser_pos, self.laser_size, self.laser_size)

        # Update trail
        self.trail.append(QPointF(self.laser_pos))
        if len(self.trail) > self.trail_length:
            self.trail.pop(0)

    def resizeEvent(self, event):
        # Ensure the laser stays within the widget when resized
        self.laser_pos = QPointF(
            min(self.laser_pos.x(), self.width()),
            min(self.laser_pos.y(), self.height())
        )

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.auto_move = not self.auto_move

    def mouseMoveEvent(self, event):
        if not self.auto_move:
            self.laser_pos = event.pos()
import random
import math
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QBrush, QPen, QPainterPath
from PyQt6.QtCore import Qt, QTimer, QPointF, QRectF

class YarnBall(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Yarn Ball")
        self.setGeometry(100, 100, 800, 600)
        self.setMouseTracking(True)

        # Yarn ball properties
        self.ball_pos = QPointF(self.width() / 2, self.height() / 2)
        self.ball_size = 50
        self.velocity = QPointF(random.uniform(-5, 5), random.uniform(-5, 5))
        self.gravity = QPointF(0, 0.5)
        self.bounce_factor = 0.8
        self.friction = 0.99
        self.yarn_color = QColor(220, 120, 120)

        # Unraveled yarn properties
        self.unraveled_yarn = []
        self.max_unravel_length = 500
        self.unravel_speed = 2

        # Mouse interaction
        self.mouse_pos = QPointF(0, 0)
        self.is_dragging = False

        # Set up timer for ball movement
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_ball)
        self.timer.start(16)  # ~60 FPS

    def update_ball(self):
        if self.is_dragging:
            # Move towards mouse when dragging
            direction = self.mouse_pos - self.ball_pos
            self.velocity = direction * 0.1
        else:
            # Apply gravity and friction
            self.velocity += self.gravity
            self.velocity *= self.friction

        # Update position
        self.ball_pos += self.velocity

        # Bounce off edges
        if self.ball_pos.x() - self.ball_size / 2 < 0 or self.ball_pos.x() + self.ball_size / 2 > self.width():
            self.velocity.setX(-self.velocity.x() * self.bounce_factor)
            self.ball_pos.setX(max(self.ball_size / 2, min(self.ball_pos.x(), self.width() - self.ball_size / 2)))

        if self.ball_pos.y() - self.ball_size / 2 < 0 or self.ball_pos.y() + self.ball_size / 2 > self.height():
            self.velocity.setY(-self.velocity.y() * self.bounce_factor)
            self.ball_pos.setY(max(self.ball_size / 2, min(self.ball_pos.y(), self.height() - self.ball_size / 2)))

        # Unravel yarn
        if self.unraveled_yarn:
            last_point = self.unraveled_yarn[-1]
            direction = self.ball_pos - last_point
            if direction.manhattanLength() > self.unravel_speed:
                new_point = last_point + direction.normalized() * self.unravel_speed
                self.unraveled_yarn.append(new_point)

                # Limit unraveled yarn length
                if len(self.unraveled_yarn) > self.max_unravel_length:
                    self.unraveled_yarn.pop(0)
        else:
            self.unraveled_yarn.append(QPointF(self.ball_pos))

        self.update()  # Trigger repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw background
        painter.fillRect(self.rect(), QColor(240, 240, 240))

        # Draw unraveled yarn
        if len(self.unraveled_yarn) > 1:
            painter.setPen(QPen(self.yarn_color, 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            path = QPainterPath()
            path.moveTo(self.unraveled_yarn[0])
            for point in self.unraveled_yarn[1:]:
                path.lineTo(point)
            painter.drawPath(path)

        # Draw yarn ball
        gradient = QRadialGradient(self.ball_pos, self.ball_size / 2)
        gradient.setColorAt(0, self.yarn_color.lighter(130))
        gradient.setColorAt(1, self.yarn_color)
        painter.setBrush(gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(self.ball_pos, self.ball_size / 2, self.ball_size / 2)

        # Draw yarn details
        painter.setPen(QPen(self.yarn_color.darker(120), 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        for i in range(6):
            angle = i * 30
            painter.drawArc(QRectF(self.ball_pos.x() - self.ball_size / 2,
                                   self.ball_pos.y() - self.ball_size / 2,
                                   self.ball_size, self.ball_size), 
                            angle * 16, 30 * 16)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = True

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False

    def mouseMoveEvent(self, event):
        self.mouse_pos = event.position()

    def resizeEvent(self, event):
        # Ensure the ball stays within the widget when resized
        self.ball_pos.setX(min(max(self.ball_pos.x(), self.ball_size / 2), self.width() - self.ball_size / 2))
        self.ball_pos.setY(min(max(self.ball_pos.y(), self.ball_size / 2), self.height() - self.ball_size / 2))
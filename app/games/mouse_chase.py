import random
from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QCursor
from PyQt6.QtCore import Qt, QTimer, QRect, QPoint
import math

class MouseChase(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Mouse Chase")
        self.setGeometry(100, 100, 800, 600)
        self.setMouseTracking(True)

        # Create mouse label
        self.mouse_label = QLabel(self)
        mouse_pixmap = QPixmap("assets/images/mouse.png")
        self.mouse_pixmap = mouse_pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.mouse_label.setPixmap(self.mouse_pixmap)
        self.mouse_label.setGeometry(0, 0, 50, 50)

        # Mouse properties
        self.mouse_speed = 5
        self.mouse_direction = random.uniform(0, 2 * math.pi)
        self.flee_distance = 150

        # Cat cursor
        cat_cursor = QPixmap("assets/images/cat_paw.png")
        cat_cursor = cat_cursor.scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.setCursor(QCursor(cat_cursor))

        # Score
        self.score = 0
        self.score_label = QLabel("Score: 0", self)
        self.score_label.setStyleSheet("color: white; font-size: 20px;")
        self.score_label.move(10, 10)

        # Set up timer for mouse movement
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_mouse)
        self.timer.start(50)  # Move every 50 ms

    def move_mouse(self):
        mouse_pos = self.mouse_label.pos()
        cursor_pos = self.mapFromGlobal(self.cursor().pos())

        # Calculate distance to cursor
        dx = cursor_pos.x() - mouse_pos.x()
        dy = cursor_pos.y() - mouse_pos.y()
        distance = math.sqrt(dx**2 + dy**2)

        # If cursor is close, flee from it
        if distance < self.flee_distance:
            angle = math.atan2(dy, dx)
            self.mouse_direction = angle + math.pi  # Flee in opposite direction
        else:
            # Randomly change direction occasionally
            if random.random() < 0.05:
                self.mouse_direction += random.uniform(-math.pi/4, math.pi/4)

        # Move in the current direction
        new_x = mouse_pos.x() + math.cos(self.mouse_direction) * self.mouse_speed
        new_y = mouse_pos.y() + math.sin(self.mouse_direction) * self.mouse_speed

        # Bounce off walls
        if new_x < 0 or new_x > self.width() - self.mouse_label.width():
            self.mouse_direction = math.pi - self.mouse_direction
            new_x = max(0, min(new_x, self.width() - self.mouse_label.width()))
        if new_y < 0 or new_y > self.height() - self.mouse_label.height():
            self.mouse_direction = -self.mouse_direction
            new_y = max(0, min(new_y, self.height() - self.mouse_label.height()))

        self.mouse_label.move(int(new_x), int(new_y))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.GlobalColor.black)

    def resizeEvent(self, event):
        # Ensure the mouse stays within the widget when resized
        if not self.rect().contains(self.mouse_label.geometry()):
            self.move_mouse()

    def mousePressEvent(self, event):
        if self.mouse_label.geometry().contains(event.pos()):
            self.score += 1
            self.score_label.setText(f"Score: {self.score}")
            self.respawn_mouse()

    def respawn_mouse(self):
        x = random.randint(0, self.width() - self.mouse_label.width())
        y = random.randint(0, self.height() - self.mouse_label.height())
        self.mouse_label.move(x, y)
        self.mouse_direction = random.uniform(0, 2 * math.pi)
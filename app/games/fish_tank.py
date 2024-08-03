import random
import math
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPolygon, QBrush, QPainterPath, QRadialGradient
from PyQt6.QtCore import Qt, QTimer, QPointF, QPoint

class Fish:
    def __init__(self, x, y, fish_type):
        self.pos = QPointF(x, y)
        self.fish_type = fish_type
        self.size = random.randint(30, 50)
        self.speed = random.uniform(1, 3)
        self.direction = self.normalize(QPointF(random.uniform(-1, 1), random.uniform(-0.5, 0.5)))
        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.tail_angle = 0
        self.tail_direction = 1

    def normalize(self, point):
        length = math.sqrt(point.x() ** 2 + point.y() ** 2)
        if length != 0:
            return QPointF(point.x() / length, point.y() / length)
        return point

    def move(self, width, height):
        new_pos = self.pos + self.direction * self.speed
        if new_pos.x() < 0 or new_pos.x() > width:
            self.direction.setX(-self.direction.x())
        if new_pos.y() < 0 or new_pos.y() > height:
            self.direction.setY(-self.direction.y())
        self.pos = new_pos
        
        # Animate tail
        self.tail_angle += self.tail_direction * 5
        if abs(self.tail_angle) > 15:
            self.tail_direction *= -1

class Bubble:
    def __init__(self, x, y):
        self.pos = QPointF(x, y)
        self.size = random.randint(5, 15)
        self.speed = random.uniform(0.5, 1.5)

    def move(self, height):
        self.pos.setY(self.pos.y() - self.speed)
        if self.pos.y() + self.size < 0:
            self.pos.setY(height + self.size)

class FishTank(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Fish Tank')
        self.fishes = [Fish(random.randint(0, 750), random.randint(0, 570), random.choice(['normal', 'angular', 'round'])) for _ in range(10)]
        self.bubbles = [Bubble(random.randint(0, 800), random.randint(0, 600)) for _ in range(20)]
        self.food = []
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_tank)
        self.timer.start(50)

    def update_tank(self):
        for fish in self.fishes:
            fish.move(self.width(), self.height())
        for bubble in self.bubbles:
            bubble.move(self.height())
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.fillRect(self.rect(), QColor(173, 216, 230))  # Light blue background

        # Draw bubbles
        painter.setPen(Qt.PenStyle.NoPen)
        for bubble in self.bubbles:
            gradient = QRadialGradient(bubble.pos, bubble.size)
            gradient.setColorAt(0, QColor(255, 255, 255, 100))
            gradient.setColorAt(1, QColor(255, 255, 255, 0))
            painter.setBrush(gradient)
            painter.drawEllipse(bubble.pos, bubble.size, bubble.size)

        # Draw fishes
        for fish in self.fishes:
            self.draw_fish(painter, fish)

        # Draw food
        painter.setBrush(QColor(200, 150, 100))
        for food_item in self.food:
            painter.drawEllipse(food_item, 3, 3)

    def draw_fish(self, painter, fish):
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(fish.color))

        path = QPainterPath()

        if fish.fish_type == 'normal':
            path.moveTo(fish.pos)
            path.cubicTo(
                fish.pos.x() - fish.size, fish.pos.y() - fish.size / 2,
                fish.pos.x() - fish.size, fish.pos.y() + fish.size / 2,
                fish.pos.x(), fish.pos.y()
            )
        elif fish.fish_type == 'angular':
            path.moveTo(fish.pos)
            path.lineTo(fish.pos.x() - fish.size, fish.pos.y() - fish.size / 2)
            path.lineTo(fish.pos.x() - fish.size, fish.pos.y() + fish.size / 2)
            path.lineTo(fish.pos)
        else:  # 'round'
            path.addEllipse(fish.pos.x() - fish.size / 2, fish.pos.y() - fish.size / 2, fish.size, fish.size)

        # Rotate the fish based on its direction
        angle = math.atan2(fish.direction.y(), fish.direction.x())
        painter.save()
        painter.translate(fish.pos)
        painter.rotate(math.degrees(angle))
        painter.translate(-fish.pos)

        painter.drawPath(path)

        # Draw tail
        tail = QPolygon([
            QPoint(int(fish.pos.x() - fish.size), int(fish.pos.y())),
            QPoint(int(fish.pos.x() - fish.size - fish.size / 2), int(fish.pos.y() - fish.size / 3)),
            QPoint(int(fish.pos.x() - fish.size - fish.size / 2), int(fish.pos.y() + fish.size / 3))
        ])
        painter.save()
        painter.translate(fish.pos.x() - fish.size, fish.pos.y())
        painter.rotate(fish.tail_angle)
        painter.translate(-(fish.pos.x() - fish.size), -fish.pos.y())
        painter.drawPolygon(tail)
        painter.restore()

        # Draw eye
        eye_pos = QPointF(fish.pos.x() + fish.size / 4, fish.pos.y())
        painter.setBrush(Qt.GlobalColor.white)
        painter.drawEllipse(eye_pos, fish.size / 10, fish.size / 10)
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(eye_pos, fish.size / 20, fish.size / 20)

        painter.restore()

    def mousePressEvent(self, event):
        self.food.append(event.pos())

    def resizeEvent(self, event):
        # Adjust fish and bubble positions if necessary when the widget is resized
        for fish in self.fishes:
            fish.pos.setX(min(fish.pos.x(), self.width()))
            fish.pos.setY(min(fish.pos.y(), self.height()))
        for bubble in self.bubbles:
            bubble.pos.setX(min(bubble.pos.x(), self.width()))
            bubble.pos.setY(min(bubble.pos.y(), self.height()))

if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    fish_tank = FishTank()
    fish_tank.show()
    sys.exit(app.exec())
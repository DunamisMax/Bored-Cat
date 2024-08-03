from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt, QSize
from PyQt6.QtGui import QFont, QIcon
import logging
import os

logger = logging.getLogger(__name__)

class GameButton(QPushButton):
    def __init__(self, text, icon_path):
        super().__init__(text)
        if os.path.exists(icon_path):
            self.setIcon(QIcon(icon_path))
        else:
            logger.warning(f"Icon not found: {icon_path}")
        self.setIconSize(QSize(32, 32))
        self.setFixedSize(200, 60)
        self.setFont(QFont("Arial", 12))
        self.setStyleSheet("""
            QPushButton {
                background-color: #2C3E50;
                color: white;
                border: 2px solid #34495E;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #34495E;
            }
            QPushButton:pressed {
                background-color: #1ABC9C;
            }
        """)

class Menu(QWidget):
    game_selected = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Title
        title_label = QLabel("Bored Cat")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #1ABC9C;")
        main_layout.addWidget(title_label)

        # Subtitle
        subtitle_label = QLabel("Choose a game to entertain your cat:")
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setFont(QFont("Arial", 14))
        subtitle_label.setStyleSheet("color: #95A5A6;")
        main_layout.addWidget(subtitle_label)

        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Game buttons
        games = [
            ("Mouse Chase", "app/assets/images/mouse_icon.png"),
            ("Laser Pointer", "app/assets/images/laser_icon.png"),
            ("Fish Tank", "app/assets/images/fish_icon.png"),
            ("Yarn Ball", "app/assets/images/yarn_icon.png")
        ]

        buttons_layout = QHBoxLayout()
        for game, icon_path in games:
            button = GameButton(game, icon_path)
            button.clicked.connect(lambda checked, g=game: self.on_game_selected(g))
            buttons_layout.addWidget(button)

        main_layout.addLayout(buttons_layout)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    def on_game_selected(self, game):
        logger.info(f"Game selected: {game}")
        self.game_selected.emit(game)

# This line is not necessary but can be helpful
__all__ = ['Menu']
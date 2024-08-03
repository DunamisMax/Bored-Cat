from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QMessageBox
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
from .menu import Menu
from .games.mouse_chase import MouseChase
from .games.laser_pointer import LaserPointer
from .games.fish_tank import FishTank
from .games.yarn_ball import YarnBall
import logging

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle("Bored Cat")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("app/assets/images/cat_icon.png"))

        # Create and set central widget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Create menu and add to central widget
        self.menu = Menu(self)
        self.central_widget.addWidget(self.menu)

        # Initialize games
        self.games = {
            "Mouse Chase": MouseChase(),
            "Laser Pointer": LaserPointer(),
            "Fish Tank": FishTank(),
            "Yarn Ball": YarnBall()
        }

        # Add games to central widget
        for game in self.games.values():
            self.central_widget.addWidget(game)

        # Connect menu signal to show_game method
        self.menu.game_selected.connect(self.show_game)

        # Create actions and menus
        self.create_actions()
        self.create_menus()

    def create_actions(self):
        # Exit action
        self.exit_action = QAction("Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.close)

        # Return to menu action
        self.return_to_menu_action = QAction("Return to Menu", self)
        self.return_to_menu_action.setShortcut("Esc")
        self.return_to_menu_action.triggered.connect(self.show_menu)

    def create_menus(self):
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")
        file_menu.addAction(self.exit_action)

        # Game menu
        game_menu = menubar.addMenu("Game")
        game_menu.addAction(self.return_to_menu_action)

    def show_game(self, game_name):
        game_widget = self.games.get(game_name)
        if game_widget:
            self.central_widget.setCurrentWidget(game_widget)
            logger.info(f"Started game: {game_name}")
        else:
            QMessageBox.warning(self, "Game Not Found", f"The game '{game_name}' is not available.")
            logger.warning(f"Attempted to start non-existent game: {game_name}")

    def show_menu(self):
        self.central_widget.setCurrentWidget(self.menu)
        logger.info("Returned to main menu")
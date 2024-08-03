"""
Bored Cat Application

This package contains the main components of the Bored Cat application,
a collection of interactive games designed to entertain cats.
"""

from .main_window import MainWindow
from .menu import Menu
from .games.mouse_chase import MouseChase
from .games.laser_pointer import LaserPointer
from .games.fish_tank import FishTank
from .games.yarn_ball import YarnBall
from .style import set_dark_theme

# Version of the application
__version__ = "1.1.0"

# List of available games
AVAILABLE_GAMES = ["Mouse Chase", "Laser Pointer", "Fish Tank", "Yarn Ball"]

# Mapping of game names to their respective classes
GAME_CLASSES = {
    "Mouse Chase": MouseChase,
    "Laser Pointer": LaserPointer,
    "Fish Tank": FishTank,
    "Yarn Ball": YarnBall
}

__all__ = [
    "MainWindow",
    "Menu",
    "MouseChase",
    "LaserPointer",
    "FishTank",
    "YarnBall",
    "AVAILABLE_GAMES",
    "GAME_CLASSES",
    "set_dark_theme"
]
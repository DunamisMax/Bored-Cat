import sys
import unittest
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMenuBar
from PyQt6.QtCore import Qt
from app.main_window import MainWindow
from app.menu import Menu
from app.games.mouse_chase import MouseChase
from app.games.laser_pointer import LaserPointer
from app.games.fish_tank import FishTank
from app.games.yarn_ball import YarnBall

class TestMainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a QApplication instance only once for all tests
        cls.app = QApplication(sys.argv)

    def setUp(self):
        # Create a fresh MainWindow instance for each test
        self.window = MainWindow()

    def test_window_title(self):
        self.assertEqual(self.window.windowTitle(), "Bored Cat")

    def test_window_geometry(self):
        self.assertEqual(self.window.geometry().size(), self.window.size())

    def test_central_widget(self):
        self.assertIsInstance(self.window.centralWidget(), QStackedWidget)

    def test_game_count(self):
        self.assertEqual(len(self.window.games), 4)

    def test_game_instances(self):
        self.assertIsInstance(self.window.games["Mouse Chase"], MouseChase)
        self.assertIsInstance(self.window.games["Laser Pointer"], LaserPointer)
        self.assertIsInstance(self.window.games["Fish Tank"], FishTank)
        self.assertIsInstance(self.window.games["Yarn Ball"], YarnBall)

    def test_menu_instance(self):
        self.assertIsInstance(self.window.menu, Menu)

    def test_menu_bar(self):
        self.assertIsInstance(self.window.menuBar(), QMenuBar)

    def test_file_menu(self):
        file_menu = self.window.menuBar().findChild(QMenuBar, "File")
        self.assertIsNotNone(file_menu)
        self.assertEqual(file_menu.title(), "File")

    def test_game_menu(self):
        game_menu = self.window.menuBar().findChild(QMenuBar, "Game")
        self.assertIsNotNone(game_menu)
        self.assertEqual(game_menu.title(), "Game")

    def test_exit_action(self):
        self.assertTrue(hasattr(self.window, 'exit_action'))
        self.assertEqual(self.window.exit_action.text(), "Exit")
        self.assertEqual(self.window.exit_action.shortcut().toString(), "Ctrl+Q")

    def test_return_to_menu_action(self):
        self.assertTrue(hasattr(self.window, 'return_to_menu_action'))
        self.assertEqual(self.window.return_to_menu_action.text(), "Return to Menu")
        self.assertEqual(self.window.return_to_menu_action.shortcut().toString(), "Esc")

    def test_show_game(self):
        self.window.show_game("Mouse Chase")
        current_widget = self.window.central_widget.currentWidget()
        self.assertIsInstance(current_widget, MouseChase)

    def test_show_menu(self):
        self.window.show_game("Mouse Chase")  # First, show a game
        self.window.show_menu()  # Then, return to menu
        current_widget = self.window.central_widget.currentWidget()
        self.assertIsInstance(current_widget, Menu)

    def test_show_nonexistent_game(self):
        with self.assertLogs(level='WARNING') as cm:
            self.window.show_game("Nonexistent Game")
        self.assertIn("Attempted to start non-existent game: Nonexistent Game", cm.output[0])

    def tearDown(self):
        self.window.close()

    @classmethod
    def tearDownClass(cls):
        # Clean up the QApplication instance
        cls.app.quit()

if __name__ == '__main__':
    unittest.main()
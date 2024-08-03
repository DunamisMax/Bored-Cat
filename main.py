import sys
import logging
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from app.main_window import MainWindow
from app.style import set_dark_theme  # Make sure this import is correct

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[logging.StreamHandler()])
    return logging.getLogger(__name__)

def exception_hook(exctype, value, traceback):
    logging.error("Uncaught exception", exc_info=(exctype, value, traceback))
    sys.__excepthook__(exctype, value, traceback)

def main():
    logger = setup_logging()
    sys.excepthook = exception_hook

    logger.info("Starting Bored Cat application")

    try:
        app = QApplication(sys.argv)
        app.setApplicationName("Bored Cat")
        app.setOrganizationName("YourOrganization")
        app.setOrganizationDomain("yourorganization.com")

        # Set the application icon
        icon_path = "app/assets/images/cat_icon.png"
        if os.path.exists(icon_path):
            app_icon = QIcon(icon_path)
            app.setWindowIcon(app_icon)
        else:
            logger.warning(f"Icon file not found: {icon_path}")

        # Apply dark theme
        set_dark_theme(app)

        window = MainWindow()
        window.show()

        logger.info("Application window displayed")

        exit_code = app.exec()
        logger.info(f"Application exiting with code {exit_code}")
        sys.exit(exit_code)

    except Exception as e:
        logger.exception("An error occurred while running the application")
        sys.exit(1)

if __name__ == "__main__":
    main()
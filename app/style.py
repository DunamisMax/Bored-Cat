from PyQt6.QtGui import QPalette, QColor

def set_dark_theme(app):
    # Set the fusion style for a more modern look
    app.setStyle("Fusion")

    # Set up the dark palette
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))

    # Apply the dark palette
    app.setPalette(dark_palette)

    # Additional stylesheet for fine-tuning
    app.setStyleSheet("""
        /* General Widget Styles */
        QWidget {
            background-color: #353535;
            color: #ffffff;
        }

        /* Tooltip Styles */
        QToolTip { 
            color: #ffffff; 
            background-color: #2a82da; 
            border: 1px solid white; 
        }

        /* Main Window Styles */
        QMainWindow::separator {
            background-color: #5a5a5a;
            width: 1px;
            height: 1px;
        }

        /* Scroll Bar Styles */
        QScrollBar:horizontal {
            border: 1px solid #222222;
            background: #333333;
            height: 15px;
            margin: 0px 20px 0 20px;
        }

        QScrollBar::handle:horizontal {
            background: #535353;
            min-width: 20px;
        }

        QScrollBar:vertical {
            border: 1px solid #222222;
            background: #333333;
            width: 15px;
            margin: 20px 0 20px 0;
        }

        QScrollBar::handle:vertical {
            background: #535353;
            min-height: 20px;
        }

        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: 1px solid #1b1b19;
            background: #515151;
        }

        /* Push Button Styles */
        QPushButton {
            background-color: #4a4a4a;
            color: #ffffff;
            border: none;
            padding: 10px;
            margin: 5px;
            font-size: 16px;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #5a5a5a;
        }

        QPushButton:pressed {
            background-color: #3a3a3a;
        }

        /* Input Widget Styles */
        QLineEdit, QTextEdit, QPlainTextEdit {
            background-color: #1e1e1e;
            color: #ffffff;
            border: 1px solid #3a3a3a;
            padding: 5px;
            border-radius: 3px;
        }

        /* Combo Box Styles */
        QComboBox {
            background-color: #4a4a4a;
            color: #ffffff;
            border: 1px solid #3a3a3a;
            padding: 5px;
            border-radius: 3px;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px;
            border-left-width: 1px;
            border-left-color: #3a3a3a;
            border-left-style: solid;
        }

        /* Menu Styles */
        QMenuBar {
            background-color: #2b2b2b;
            color: #ffffff;
        }

        QMenuBar::item:selected {
            background-color: #3a3a3a;
        }

        QMenu {
            background-color: #2b2b2b;
            color: #ffffff;
        }

        QMenu::item:selected {
            background-color: #3a3a3a;
        }

        /* Tab Widget Styles */
        QTabWidget::pane {
            border-top: 2px solid #3a3a3a;
        }

        QTabBar::tab {
            background-color: #2b2b2b;
            color: #b1b1b1;
            padding: 8px 12px;
            margin-right: 2px;
        }

        QTabBar::tab:selected {
            background-color: #3a3a3a;
            color: #ffffff;
        }

        /* Progress Bar Styles */
        QProgressBar {
            border: 2px solid #3a3a3a;
            border-radius: 5px;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: #2a82da;
            width: 10px;
            margin: 0.5px;
        }

        /* Group Box Styles */
        QGroupBox {
            border: 1px solid #3a3a3a;
            border-radius: 5px;
            margin-top: 10px;
            padding-top: 10px;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding: 0 3px;
            color: #ffffff;
        }

        /* Label Styles */
        QLabel {
            color: #ffffff;
        }

        /* Tool Bar Styles */
        QToolBar {
            background-color: #2b2b2b;
            border: none;
        }

        QToolBar::separator {
            background-color: #3a3a3a;
            width: 1px;
            height: 1px;
        }
    """)
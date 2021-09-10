#IMPORT MODULES
import sys
import os

#IMPORT QT CORE
from qt_core import *

#IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import *


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    
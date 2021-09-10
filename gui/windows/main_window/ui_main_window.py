from qt_core import *

# MAIN WINDOW
class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # WINDOW SIZE
        w = 600 # WIDTH 300
        h = 600 # HEIGHT 450
        parent.setFixedSize(w, h)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282a36")


        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setFixedSize(w*0.1, h)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setFixedSize(w, h*0.05)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size:12pt; color: #6272a4")

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # ADD WIDGET TO CONTENT LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)

        # ADD WIDGET TO APP 
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)


        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame )
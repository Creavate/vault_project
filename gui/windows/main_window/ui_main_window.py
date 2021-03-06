from qt_core import *

# IMPORTING PAGES
from gui.pages.ui_pages import Pages

# MAIN WINDOW
class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # WINDOW SIZE
        w = 1200 # WIDTH 300
        h = 720 # HEIGHT 450
        parent.resize(w,h)
        parent.setMinimumSize(960,540)

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
        self.left_menu.setMaximumWidth(50)

        # LEFT MENU LAYOUT 
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)
        
        # LEFT MENU TOP FRAME
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setStyleSheet('background-color: red')


        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMinimumWidth(30)        
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")      
  

        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size:12pt; color: #6272a4; background-color: black")
        self.ui_pages = Pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)

        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setFixedSize(w - self.left_menu.width(), h*0.05)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # ADD WIDGET TO CONTENT LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD WIDGET TO APP 
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)




        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame )
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from modules import *
import sys
import os

class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow,self).__init__(*args,**kwargs)
        #setting property value variables
        self.title="Gene BrowsePad"
        self.top=0
        self.left=0
        self.height=1020
        self.width=2000

        #initializing Layout
        hbox = QHBoxLayout()

        #get built browser window from Browser class
        browser = Browser()

        #for having two sub-windows in same window
        splitWindow = QSplitter(Qt.Horizontal)
        lineedit =MyNote()

        splitWindow.addWidget(browser)
        splitWindow.addWidget(lineedit)
        splitWindow.setSizes([200,200])
        hbox.addWidget(splitWindow)

        #setting layout
        self.setLayout(hbox)
        self.setWindowIcon(QIcon(os.path.join('icons',"logo.png")))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

#instantiating application
App = QApplication(sys.argv)
window = MyWindow()
#running app
sys.exit(App.exec())

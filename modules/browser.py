from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import os

class Browser(QMainWindow):
    def __init__(self,*args,**kwargs):
        #initialising window
        super(Browser,self).__init__(*args,**kwargs)

        #adding browser property (surfability)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)
        self.stylesheet="""
            QLineEdit{
                border-width:5px;
                border-radius:20px;
                height:40px;
            }
        """

        #navigation bar
        navToolBar= QToolBar("Navigation")
        navToolBar.setIconSize(QSize(64,64))
        self.addToolBar(navToolBar)

        #back button
        backButton=QAction(QIcon(os.path.join('icons','back.png')),"Back",self)
        backButton.setStatusTip("Previous page")
        backButton.triggered.connect(self.browser.back)
        navToolBar.addAction(backButton) 

        #next button
        nextButton=QAction(QIcon(os.path.join('icons','next.png')),"Next",self)
        nextButton.setStatusTip("Next page")
        nextButton.triggered.connect( self.browser.forward)
        navToolBar.addAction(nextButton) 

        #home button
        homeButton=QAction(QIcon(os.path.join('icons','home.png')),"Home",self)
        homeButton.setStatusTip("Home page")
        homeButton.triggered.connect(self.navigateHome)
        navToolBar.addAction(homeButton)

        #reload button
        reloadButton=QAction(QIcon(os.path.join('icons','reload.png')),"Reload",self)
        reloadButton.setStatusTip("Reload the page")
        reloadButton.triggered.connect(self.browser.reload)
        navToolBar.addAction(reloadButton)

        navToolBar.addSeparator()

        #for secure websites
        self.httpsicon =QLabel()
        navToolBar.addWidget(self.httpsicon)
        

        #address bar
        self.urlbar =QLineEdit()
        self.urlbar.returnPressed.connect(self.navigateTo)
        navToolBar.addWidget(self.urlbar)

        #stop button
        stopButton=QAction(QIcon(os.path.join('icons','close.png')),"Close",self)
        stopButton.setStatusTip("stop")
        stopButton.triggered.connect(self.browser.stop)
        navToolBar.addAction(stopButton)

        self.browser.urlChanged.connect( self.updateURL)

        #style applied
        self.setStyleSheet(self.stylesheet)

        #shows the window after ready
        self.show()
        self.setWindowTitle("Gene")
        self.setWindowIcon(QIcon(os.path.join('icons','gene.png')))
        self.screenWidth, self.screenHeight = self.geometry().width(), self.geometry().height()
        self.resize(self.screenWidth * 2, self.screenHeight * 2)

    def navigateHome(self):
        #redirect to home
        self.browser.setUrl(QUrl("http://www.google.com"))

    def updateURL(self,q):
    #for updating icon based on http or https
        if q.scheme() == 'https':
            self.httpsicon.setPixmap( QPixmap(os.path.join('icons','lock.png')))
        else:
            self.httpsicon.setPixmap( QPixmap(os.path.join('icons','nonlock.png')))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def navigateTo(self):
        #getting URL
        q=QUrl(self.urlbar.text())
        if q.scheme() == "":
            #setting default http scheme if https is not set
            q.setScheme("http")
        
        #calling the requested URL
        self.browser.setUrl(q)

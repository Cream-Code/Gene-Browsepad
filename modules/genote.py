import sys,os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from syntaxhighlighters.Python import PythonHighlighter
from syntaxhighlighters.Html import HtmlHighlighter
from syntaxhighlighters.css import CssHighlighter
from syntaxhighlighters.JavaScript import JavaScriptHighlighter

class MyNote(QMainWindow):
    def __init__(self,browser):
        super().__init__()
        
        #setting files supported file types         
        self.filterTypes='All(*.*);;Text Document(*.txt);;Python(*.py);;Markdown(*.md);;CSS style sheet(*.css);;html(*.html);;Java script(*.js)'
        
        #path for file location
        self.path=None

        #adding browser object
        self.browser=browser

        #highlight variable for language specific highlight
        self.highlighter = None

        #box layout for arranging elements
        mainLayout=QVBoxLayout()

        #editor - area for typing file text
        self.setStyleSheet("QPlainTextEdit,QMainWindow{font-family:Consolas; font-size:18px; color: #fff; background-color: #2b2b2b; selection: white;}")
        self.editor=QPlainTextEdit()
        mainLayout.addWidget(self.editor)
        self.setStyleSheet("QWidget{font-family:Consolas; font-size:18px; color: #fff; background-color: #2b2b2b; selection: white;}")

        #statusBar
        self.statusBar=self.statusBar()

        #app container
        container=QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

        #file menu '&' used for shortcuts
        fileMenu=self.menuBar().addMenu('&File')

        #file ToolBar
        fileToolbar=QToolBar('File')
        fileToolbar.setIconSize(QSize(32,32))
        self.addToolBar(Qt.TopToolBarArea,fileToolbar)

        '''open,save,saveAs - actions using QAcction'''
        openFileAction=QAction(QIcon(os.path.join('icons',"open.png")),'Open File...',self)
        openFileAction.setStatusTip('Open file')
        openFileAction.setShortcut(QKeySequence.Open)
        openFileAction.triggered.connect(self.fileOpen)

        #saving a file
        saveFileAction=self.createAction(self,os.path.join('icons',"save.png"),"Save File","save file",self.fileSave)
        saveFileAction.setShortcut(QKeySequence.Save)

        #save with other name - Save as
        saveFileAsAction=self.createAction(self,os.path.join('icons',"saveas.png"),"Save File As...","save file as",self.fileSaveAs)
        saveFileAsAction.setShortcut(QKeySequence('Ctrl+Shift+S'))

        fileMenu.addActions([openFileAction,saveFileAction,saveFileAsAction])
        fileToolbar.addActions([openFileAction,saveFileAction,saveFileAsAction])

        #print Acton used to print files opened
        printAction=self.createAction(self,os.path.join('icons',"print.png"),"Print File","print file",self.printFile)
        printAction.setShortcut(QKeySequence.Print)
        fileMenu.addAction(printAction)
        fileToolbar.addAction(printAction)

        #Edits menu
        editMenu=self.menuBar().addMenu('&Edit')

        #Edits toolbar
        editToolbar=QToolBar('Edit')
        editToolbar.setIconSize(QSize(32,32))
        self.addToolBar(Qt.TopToolBarArea,editToolbar)

        #undo,redo actions

        undoAction=self.createAction(self,os.path.join('icons',"undo.png"),"Undo",'undo',self.editor.undo)
        undoAction.setShortcut(QKeySequence.Undo)

        redoAction=self.createAction(self,os.path.join('icons',"redo.png"),"Redo",'redo',self.editor.redo)
        redoAction.setShortcut(QKeySequence.Redo)

        editMenu.addActions([undoAction,redoAction])
        editToolbar.addActions([undoAction,redoAction])

        
        #add seperator
        editMenu.addSeparator()
        editToolbar.addSeparator()

        #cut,copy,paste,select all
        cutAction=self.createAction(self,os.path.join('icons',"cut.png"),"Cut",'cut',self.editor.cut)
        copyAction=self.createAction(self,os.path.join('icons',"copy.png"),"Copy",'copy',self.editor.copy)
        pasteAction=self.createAction(self,os.path.join('icons',"paste.png"),"Paste",'paste',self.editor.paste)
        

        cutAction.setShortcut(QKeySequence.Cut)
        copyAction.setShortcut(QKeySequence.Copy)
        pasteAction.setShortcut(QKeySequence.Paste)
        

        editMenu.addActions([cutAction,copyAction,pasteAction,])
        editToolbar.addActions([cutAction,copyAction,pasteAction,])

        #add seperator
        editMenu.addSeparator()
        editToolbar.addSeparator()

        languagesToolbar = QToolBar("Languages")
        languagesToolbar.setIconSize(QSize(40, 40))
        self.addToolBar(languagesToolbar)
        languagesMenu = self.menuBar().addMenu("&Languages")

        #set syntax to python
        pythonAction = QAction(QIcon(os.path.join('icons', 'python.png')), "Python", self)
        pythonAction.setStatusTip("Python")
        pythonAction.triggered.connect(self.python)
        languagesMenu.addAction(pythonAction)
        languagesToolbar.addAction(pythonAction)

        

        #set syntax to html
        htmlAction = QAction(QIcon(os.path.join('icons', 'html.png')), "Html", self)
        htmlAction.setStatusTip("Html")
        htmlAction.triggered.connect(self.html)
        languagesMenu.addAction(htmlAction)
        languagesToolbar.addAction(htmlAction)

        #set syntax to css
        cssAction = QAction(QIcon(os.path.join('icons', 'css.png')), "css", self)
        cssAction.setStatusTip("css")
        cssAction.triggered.connect(self.css)
        languagesMenu.addAction(cssAction)
        languagesToolbar.addAction(cssAction)

        #set syntax to JavaScript
        jsAction = QAction(QIcon(os.path.join('icons', 'js.png')), "JavaScript", self)
        jsAction.setStatusTip("JavaScript")
        jsAction.triggered.connect(self.JavaScript)
        languagesMenu.addAction(jsAction)
        languagesToolbar.addAction(jsAction)
        
        
    def toggleWrapText(self):
        self.editor.setLineWrapMode(not self.editor.lineWrapMode())
        
    def clearContent(self):
        self.editor.setPlainText('')
        
    def fileOpen(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")
        if path:
            try:
                with open(path,'r') as f:
                    text=f.read()
                    f.close()
                self.redirect(path)
            except Exception as e:
                self.dialogMessage(str(e))
            else:
                self.path=path
                self.editor.setPlainText(text)

    def fileSave(self):
        if self.path is None:
            self.fileSaveAs()
        else:
            try:
                text = self.editor.toPlainText()
                with open(self.path, 'w') as f:
                    f.write(text)
                    f.close()
                self.redirect(self.path)
            except Exception as e:  
                self.dialogMessage(str(e))
    
    def fileSaveAs(self):
        path, _ = QFileDialog.getSaveFileName(self,'Save file as','',self.filterTypes)                               
        text = self.editor.toPlainText()
        if not path:
            return
        else:
            try:
                with open(path, 'w') as f:
                    f.write(text)
                    f.close()
                self.redirect(path)
            except Exception as e:
                self.dialogMessage(str(e))
            else:
                self.path = path

    def redirect(self,path):
        #refreshing browser with edited file to see html output
        self.browser.updateURL(QUrl('file:///'+path))
        self.browser.navigateTo()
        
    def printFile(self):
        printDialog=QPrintDialog()
        if printDialog.exec_():
            self.editor.print_(printDialog.printer())


                
    def dialogMessage(self,message):
        dig=QMessageBox(self)
        dig.setText(message)
        dig.setIcon(QMessageBox.Critical)
        dig.show()
        
    def createAction(self,parent,iconPath,actionName,setStatusTip,triggeredMethod):
        action=QAction(QIcon(iconPath),actionName,parent)
        action.setStatusTip(setStatusTip)
        action.triggered.connect(triggeredMethod)
        return action
    def python(self):
        self.highlighter = PythonHighlighter(self.editor.document())
    def html(self):
        self.highlighter = HtmlHighlighter(self.editor.document())
    def css(self):
        self.highlighter = CssHighlighter(self.editor.document())
    def JavaScript(self):
        self.highlighter = JavaScriptHighlighter(self.editor.document())    
        

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets \
    import QMainWindow, QLabel, QGridLayout, QWidget, QMessageBox, QPushButton, QAction, QLineEdit, QPlainTextEdit
from PyQt5.QtCore import QSize


class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.max_rows=0
        self.max_cols=0

        self.menu = None
        self.textBox = None
        self.textArea = None
        self.logArea = None

    def winSetup(self,windowTitle="Default Window Title", width=640, height=480):
        self.setMinimumSize(QSize(width,height))
        self.setWindowTitle(windowTitle)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # grid_layout == (row,col) == from (0,0)
        self.gridLayout = QGridLayout(self)
        self.centralWidget.setLayout(self.gridLayout)

    def update_grid(self,row,col):
        if row > self.max_rows:
            self.max_rows = row
        if col > self.max_cols:
            self.max_cols = col

    def addLabel(self, text, row=0, col=0, align=None):
        label = QLabel(text, self)
        if align is not None:
            if align == 'r' or align == 'R':
                label.setAlignment(QtCore.Qt.AlignRight)
            elif align == 'l' or align == 'L':
                label.setAlignment(QtCore.Qt.AlignLeft)
            elif align == 'c' or align == 'C':
                label.setAlignment(QtCore.Qt.AlignCenter)
        self.placeWidget(label,row,col)


    def callbackButton(self):
        self.addMessageBox(mesg='Clicked PyQt5 Button')

    def addButton(self,text,clickmethod,row=0,col=0):
        pybutton = QPushButton(text,self)
        pybutton.clicked.connect(clickmethod)
        self.placeWidget(pybutton,row,col)

    def addTextBox(self,label='Default Label',text='Default Text', row=0, col=0):
        self.addLabel(label, row, col, align='R')
        col += 1
        self.textBox = QLineEdit(self)
        self.placeWidget(self.textBox,row,col)

    def addTextArea(self,row=0,col=0):
        self.textArea = QPlainTextEdit(self)
        self.placeWidget(self.textArea,row,col)

    def addLogArea(self,row=0,col=0, colspan=1):
        self.logArea = QPlainTextEdit(self)
        self.logArea.setReadOnly(True)
        self.placeWidget(self.logArea,row,col,colspan)

    def addLog(self,text):
        if self.logArea is None:
            self.addLogArea(99, 0, -1)

        self.logArea.appendPlainText(text)

    def clearWidget(self,widget=None):
        if widget is not None:
            widget.clear()

    def clearAll(self):
        self.clearWidget(self.logArea)
        self.clearWidget(self.textArea)
        self.clearWidget(self.textBox)

    # --------------------------------------------------------------------
    def placeWidget(self, widget, row, col, colspan=None):
        if colspan is None:
            colspan=1

        self.gridLayout.addWidget(widget,row,col,1,colspan)
        self.update_grid(row,col)

    def addMessageBox(self, title="Default Title", mesg="Default Message"):
        QMessageBox.about(self, title, mesg)

    def addTopMenu(self, title):
        if self.menu is None:
            self.menu = self.menuBar()
        return(self.menu.addMenu(title))

    def callbackMenuItem(self):
        self.addMessageBox(mesg='Clicked PyQt5 MenuItem')

    def addMenuItem(self,topMenu,title,menuMethod, shortcut=None):
        action = QAction(title, self)
        action.triggered.connect(menuMethod)
        if shortcut is not None:
            action.setShortcut(shortcut)
        topMenu.addAction(action)

    # -----------------------------------------------------------------------
    def debug_print_textBoxContents(self):
        # self.addMessageBox(mesg=self.textBox.text())
        self.addLog(self.textBox.text())

    def debug_print_textAreaContents(self):
        # self.addMessageBox(mesg=self.textArea.toPlainText())
        self.addLog(self.textArea.toPlainText())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.winSetup(windowTitle='Hello World', width=500, height=100)
    row=0
    mainWin.addLabel('Hello World from PyQt5', row, 0)
    mainWin.addLog('Label Added')

    row += 1
    mainWin.addTextBox('Name', row=row,col=0)
    mainWin.addButton('Test', mainWin.debug_print_textBoxContents, row, 5)
    mainWin.addLog('TextBox Added')

    row += 1
    mainWin.addTextArea(row=row,col=0)
    mainWin.addButton('Test', mainWin.debug_print_textAreaContents, row, 5)
    mainWin.addLog('TextArea Added')

    row += 1
    mainWin.addButton('Click Me', mainWin.callbackButton, row, 5)
    mainWin.addButton('Clear', mainWin.clearAll, row, 6)
    mainWin.addButton('Exit', sys.exit, row, 7)
    mainWin.addLog('Button Added')

    fileMenu = mainWin.addTopMenu('&File')
    mainWin.addMenuItem(fileMenu, '&New', mainWin.callbackMenuItem)
    mainWin.addMenuItem(fileMenu, '&Open', mainWin.callbackMenuItem, shortcut='Ctrl+O')
    mainWin.addMenuItem(fileMenu, '&Quit', sys.exit, shortcut='Ctrl+Q')
    mainWin.addLog('Menu Added')
    # mainWin.addMessageBox('MsgTitle','Hello World from PyQt5 MessageBox')   # Last, but this still pops up first
    mainWin.show()
    sys.exit(app.exec_())

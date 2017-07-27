#!/usr/bin/python3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os

class App(QApplication):
    # Main application

    # Input: command line arguments <list>
    # Output: None

    def __init__(self):
        # Initialize parent widget
        QApplication.__init__(self, sys.argv)

        # Set application name
        self.setApplicationName("Eavesdropping GUI")

        # Create main window
        self.mainWindow = MainWindow()

        # Show main window
        self.mainWindow.show()


class MainWindow(QMainWindow):
    # Main GUI window

    def __init__(self):

        # Initialize parent widget
        QMainWindow.__init__(self)

        # Initialize this window
        self.setWindowTitle("Eavesdropping Demo")

        # Set the size of the main window
        self.resize(1, 1)

        # Create a main widget object (the central widget)
        self.mainWidget = MainWidget()

        # Set main widget object as central widget of main window
        self.setCentralWidget(self.mainWidget)

        # Add file menu with exit action
        self.fileMenu = QMenu("File")
        self.exit = QAction("Exit", self)

        # Set exit icon
        self.exit.setIcon(QIcon(os.path.join(sys.path[0], "icons", "exit.png")))
        self.exit.triggered.connect(self.close)
        self.fileMenu.addAction(self.exit)

        # Add file menu to menu bar
        self.menuBar().addMenu(self.fileMenu)

        # Add exit to tool bar
        self.toolBar = QToolBar()
        self.toolBar.addAction(self.exit)
        self.addToolBar(self.toolBar)


    def closeEvent(self, event):
        # Override the default close event actions. This even runs
        # whenever the application closes.
        print("Application closed")
        QMainWindow.closeEvent(self, event)


class MainWidget(QWidget):
    # Central widget, contains widgets and layouts

    def __init__(self):
        QWidget.__init__(self)

        # Create main layout and close button
        self.mainLayout = QHBoxLayout(self)
        self.clientLayout = QVBoxLayout()
        self.snifferLayout = QVBoxLayout()
        self.serverLayout = QVBoxLayout()

        ######################
        # Client functionality
        ######################
        self.clientHeader = QLabel("Client")
        self.clientLayout.addWidget(self.clientHeader, alignment=Qt.AlignHCenter)
        self.sentMessages = QPlainTextEdit()
        self.sentMessages.setReadOnly(True)
        self.clientLayout.addWidget(self.sentMessages)

        ## Send mesage layout
        self.sendMessageLayout = QHBoxLayout()
        self.messageLineEdit = QLineEdit()
        sendMessageButtonText = "Send"
        self.sendMessageButton = QPushButton(sendMessageButtonText)
        self.sendMessageButton.clicked.connect(self.sendMessage)
        self.sendMessageLayout.addWidget(self.messageLineEdit)
        self.sendMessageLayout.addWidget(self.sendMessageButton)
        self.clientLayout.addLayout(self.sendMessageLayout)

        ## Fix widget sizes
        sentMessagesHeight = 300
        messageLineEditWidth = 300
        sendMessageButtonWidth = self.sendMessageButton.fontMetrics().boundingRect(sendMessageButtonText).width() + 7
        self.sentMessages.setFixedWidth(sendMessageButtonWidth + messageLineEditWidth)
        self.sentMessages.setFixedHeight(sentMessagesHeight)
        self.sendMessageButton.setFixedWidth(sendMessageButtonWidth)
        self.messageLineEdit.setFixedWidth(messageLineEditWidth)

        ######################
        # Server functionality
        ######################
        self.serverHeader = QLabel("Server")
        self.serverLayout.addWidget(self.serverHeader, alignment=Qt.AlignHCenter)
        self.receivedMessages = QPlainTextEdit()
        self.receivedMessages.setReadOnly(True)
        self.serverLayout.addWidget(self.receivedMessages)

        ## Fix widget sizes
        self.receivedMessages.setFixedWidth(self.sentMessages.width())

        # Vertical separator
        self.vline1 = QFrame()
        self.vline1.setFrameStyle(QFrame.VLine)
        self.vline1.setFrameShadow(QFrame.Sunken)
        self.vline2 = QFrame()
        self.vline2.setFrameStyle(QFrame.VLine)
        self.vline2.setFrameShadow(QFrame.Sunken)

        # Add button to bottom of page
        self.mainLayout.addLayout(self.clientLayout)
        self.mainLayout.addWidget(self.vline1)
        self.mainLayout.addLayout(self.snifferLayout)
        self.mainLayout.addWidget(self.vline2)
        self.mainLayout.addLayout(self.serverLayout)

    def sendMessage(self):
        self.sentMessages.appendPlainText('[SENT]  '+self.messageLineEdit.text())
        self.messageLineEdit.clear()

class Thread(QThread):
    ''' Thread object to handle client/server '''
    def __init__(self, path):
        QThread.__init__(self)
        self.path = path

    def run(self):
        os.system(self.path)

def main():
    # Create application
    app = App()

    # Start event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


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
        self.setApplicationName("Toolkit Launcher")

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
        self.setWindowTitle("Toolkit Launcher")

        # Set the size of the main window
        self.resize(240, 200)

        # Create a main widget object (the central widget)
        self.mainWidget = MainWidget()
        
        # Set main widget object as central widget of main window
        self.setCentralWidget(self.mainWidget)

        # Add Close button functionality
        self.mainWidget.closeButton.clicked.connect(self.close)

    def closeEvent(self, event):
        # Override the default close event actions. This even runs
        # whenever the application closes.
        print("Application closed")
        QMainWindow.closeEvent(self, event)


class MainWidget(QWidget):
    # Central widget, contains widgets and layouts

    def __init__(self):
        QWidget.__init__(self)

        # Create main layout and launch buttons
        self.mainLayout = QVBoxLayout(self)
        self.sqliButton = QPushButton("SQL injetion")
        self.sqliButton.clicked.connect(self.launchSQLi)
        self.eavesdroppingButton = QPushButton("Eavesdropping")
        self.eavesdroppingButton.clicked.connect(self.launchEavesdropping)
        self.steganographyButton = QPushButton("Steganography")
        self.steganographyButton.clicked.connect(self.launchSteganoggraphy)

        # Create close button
        self.closeButton = QPushButton("Close")

        # Add button to bottom of page
        self.mainLayout.addWidget(self.sqliButton, alignment=Qt.AlignHCenter)
        self.mainLayout.addWidget(self.eavesdroppingButton, alignment=Qt.AlignHCenter)
        self.mainLayout.addWidget(self.steganographyButton, alignment=Qt.AlignHCenter)
        self.mainLayout.addWidget(self.closeButton, alignment=Qt.AlignBottom)
    
    def launchSQLi(self):
        pass
    def launchEavesdropping(self):
        pass
    def launchSteganoggraphy(self):
        print(os.path.join(sys.path[0], "steganograpy", "encodeGUI.py"))
        os.system(os.path.join(sys.path[0], "steganograpy", "encodeGUI.py"))
        


def main():
    # Create application
    app = App()

    # Start event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

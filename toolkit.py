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
        self.mainWidget.close_button.clicked.connect(self.close)

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

        self.sqli_layout = QHBoxLayout()
        self.sqli_label = QLabel("SQL Injection")
        self.sqli_info_button = QPushButton("Info")
        self.sqli_info_button.clicked.connect(self.sqli_info) 
        self.sqli_button = QPushButton("Launch demo")
        self.sqli_button.clicked.connect(self.launchSQLi)
        self.sqli_layout.addWidget(self.sqli_info_button)
        self.sqli_layout.addWidget(self.sqli_button)

        self.eavesdropping_layout = QHBoxLayout()
        self.eavesdropping_label = QLabel("Eavesdropping")
        self.eavesdropping_info_button = QPushButton("Info")
        self.eavesdropping_info_button.clicked.connect(self.eavesdropping_info)
        self.eavesdropping_button = QPushButton("Launch demo")
        self.eavesdropping_button.clicked.connect(self.launch_eavesdropping)
        self.eavesdropping_layout.addWidget(self.eavesdropping_info_button)
        self.eavesdropping_layout.addWidget(self.eavesdropping_button)

        self.steganography_layout = QHBoxLayout()
        self.steganography_label = QLabel("Steganography")
        self.steganography_info_button = QPushButton("Info")
        self.steganography_encode_button = QPushButton("Encode")
        self.steganography_decode_button = QPushButton("Decode")
        self.steganography_info_button.clicked.connect(self.steganography_info)
        self.steganography_encode_button.clicked.connect(self.launch_steganoggraphy_encode)
        self.steganography_decode_button.clicked.connect(self.launch_steganoggraphy_decode)
        self.steganography_layout.addWidget(self.steganography_info_button)
        self.steganography_layout.addWidget(self.steganography_encode_button)
        self.steganography_layout.addWidget(self.steganography_decode_button)

        # Create close button
        self.close_button = QPushButton("Close")

        # Add button to bottom of page
        self.mainLayout.addWidget(self.sqli_label)
        self.mainLayout.addLayout(self.sqli_layout)
        self.mainLayout.addWidget(self.eavesdropping_label)
        self.mainLayout.addLayout(self.eavesdropping_layout)
        self.mainLayout.addWidget(self.steganography_label)
        self.mainLayout.addLayout(self.steganography_layout)
        self.mainLayout.addWidget(self.close_button)#, alignment=Qt.AlignBottom)
    
    def sqli_info(self):
        self.info = QMessageBox()
        self.info.exec()
    def launchSQLi(self):
        pass

    def eavesdropping_info(self):
        pass
    def launch_eavesdropping(self):
        pass

    def steganography_info(self):
        pass
    def launch_steganoggraphy_encode(self):
        os.system(os.path.join(sys.path[0], "steganography", "encodeGUI.py"))
    def launch_steganoggraphy_decode(self):
        os.system(os.path.join(sys.path[0], "steganography", "decodeGUI.py"))
        


def main():
    # Create application
    app = App()

    # Start event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

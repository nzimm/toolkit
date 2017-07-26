#!/usr/bin/python3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os
import time
import webbrowser

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

        # Main layout
        self.mainLayout = QVBoxLayout(self)

        # SQL injection layout/buttons
        self.sqli_layout = QHBoxLayout()
        self.sqli_label = QLabel("SQL Injection")
        self.sqli_info_button = QPushButton("Info")
        self.sqli_info_button.clicked.connect(self.sqli_info) 
        self.sqli_button = QPushButton("Launch demo")
        self.sqli_button.clicked.connect(self.launchSQLi)
        self.sqli_layout.addWidget(self.sqli_info_button)
        self.sqli_layout.addWidget(self.sqli_button)

        # Eavesdropping layout/buttons
        self.eavesdropping_header_layout = QHBoxLayout()
        self.eavesdropping_label = QLabel("Eavesdropping")
        self.encryptFlag = QCheckBox("Encrypt")
        self.eavesdropping_header_layout.addWidget(self.eavesdropping_label)
        self.eavesdropping_header_layout.addWidget(self.encryptFlag)
        self.eavesdropping_layout = QHBoxLayout()
        self.eavesdropping_info_button = QPushButton("Info")
        self.eavesdropping_info_button.clicked.connect(self.eavesdropping_info)
        self.eavesdropping_button = QPushButton("Launch demo")
        self.eavesdropping_button.clicked.connect(self.launch_eavesdropping)
        self.eavesdropping_layout.addWidget(self.eavesdropping_info_button)
        self.eavesdropping_layout.addWidget(self.eavesdropping_button)

        # Steganography layout/buttons
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

        # Create close button and horizontal separators
        self.close_button = QPushButton("Close")
        self.horizontal_line1 = QFrame()
        self.horizontal_line1.setFrameStyle(QFrame.HLine)
        self.horizontal_line1.setFrameShadow(QFrame.Sunken)
        self.horizontal_line2 = QFrame()
        self.horizontal_line2.setFrameStyle(QFrame.HLine)
        self.horizontal_line2.setFrameShadow(QFrame.Sunken)
        self.horizontal_line3 = QFrame()
        self.horizontal_line3.setFrameStyle(QFrame.HLine)
        self.horizontal_line3.setFrameShadow(QFrame.Sunken)

        # Compile main layout
        self.mainLayout.addWidget(self.sqli_label)
        self.mainLayout.addLayout(self.sqli_layout)
        self.mainLayout.addWidget(self.horizontal_line1)
        self.mainLayout.addLayout(self.eavesdropping_header_layout)
        self.mainLayout.addLayout(self.eavesdropping_layout)
        self.mainLayout.addWidget(self.horizontal_line2)
        self.mainLayout.addWidget(self.steganography_label)
        self.mainLayout.addLayout(self.steganography_layout)
        self.mainLayout.addWidget(self.horizontal_line3)
        self.mainLayout.addWidget(self.close_button)
    
    def sqli_info(self):
        self.info = QMessageBox()
        self.info.setWindowTitle("SQL injection introduction")
        self.info.setText("SQL injection is a classic example of an injection vulnerability. It manifests "
                          "when a SQL query is handled incorrectly. The most common occurance of this is "
                          "when a programmer concatenates a query with user-controlled input. This gives "
                          "the user full control of the sql query. This issue can be resolved by using SQL "
                          "parameters. User input is then read in as a single field, rather than a string of "
                          "code.\n\nExample query:\n\"SELECT username FROM users WHERE firstname=\" + get_user_info + \";"
                          "\nIf the user entered a string similar to `john OR 1=1;` the WHERE clause would evaluate to "
                          "true, and the query would SELECT every username.")
        self.info.exec()

    def launchSQLi(self):
        self.serverThread = Thread(os.path.join(sys.path[0], "sqli", "server.py"))
        self.serverThread.start()
        time.sleep(1)
        webbrowser.open_new('http://127.0.0.1:8080')

    def eavesdropping_info(self):
        self.info = QMessageBox()
        self.info.setWindowTitle("Packet sniffing introduction")
        self.info.setText("Eavesdropping, in the context of computers and networks, typically refers to tapping "
                          "a communication channel, and collecting the data as if flows. This demonstration shows "
                          "how an attacker can eavesdrop on network traffic, and read data as if is transfered "
                          "through the network. Additionally, the user may encrypt their traffic, and the plaintext "
                          "data becomes garbeled bits.\n\nWhile all packets are passed through the internal loopback, "
                          "the implementation is nearly identical to tapping any TCP connection on the internet.")
        self.info.exec()

    def launch_eavesdropping(self):
        # TODO find a way to run client, server, and sniffer in qt so that the stdout
        #      prints on a widget, and the input to qt goes to the process
        if self.encryptFlag.checkState():
            print("Encrypt")
        else:
            print("No encrypt")

    def steganography_info(self):
        self.info = QMessageBox()
        self.info.setWindowTitle("Steganography introduction")
        self.info.setText("Steganography is the practice of hiding data 'in plain sight'. Different from "
                          "encryption, steganography conceals data inside other files. For instance, someone "
                          "might hide a message as the first letter of each line in a blog post. The algorithm "
                          "used in the demonstration is refered to as the Least Significant Bit algorithm, "
                          "wherein one bit of the message is encoded in the LSB of each color of a pixel in "
                          "an image. For someone to decode the message, they must have knowledge of the algorithm "
                          "with which it was encoded.\n\nThe encoding program gives the user a preview of the "
                          "image with the message encoded, so they may visually inspect the image for any givaways "
                          "that there is data encoded. A 1-bit change in a color is nearly indistinguishable to the "
                          "human eye, which is why this technique is so powerful.")
        self.info.exec()

    def launch_steganoggraphy_encode(self):
        self.encodeThread = Thread(os.path.join(sys.path[0], "steganography", "encodeGUI.py"))
        self.encodeThread.start()
    def launch_steganoggraphy_decode(self):
        self.decodeThread = Thread(os.path.join(sys.path[0], "steganography", "decodeGUI.py"))
        self.decodeThread.start()
        
class Thread(QThread):
    ''' Thread object to handle running demos '''
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

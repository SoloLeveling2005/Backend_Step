import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon
from PyQt5.uic import loadUi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Load the .ui file
    window = QMainWindow()
    # window.setWindowTitle('Random image download')
    loadUi('design.ui', window)

    window.show()

    sys.exit(app.exec_())
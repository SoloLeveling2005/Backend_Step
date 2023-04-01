# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon
# from PyQt5.uic import loadUi
#
#
# def download_zip_file(url, save_path):
#     manager = QNetworkAccessManager()
#     request = QNetworkRequest(QUrl(url))
#     reply = manager.get(request)
#
#     def save_file():
#         if reply.error():
#             print(reply.errorString())
#         else:
#             with open(save_path, 'wb') as f:
#                 f.write(reply.readAll())
#
#         reply.deleteLater()
#
#     reply.finished.connect(save_file)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     # Load the .ui file
#     window = QMainWindow()
#     # window.setWindowTitle('Random image download')
#     loadUi('design.ui', window)
#
#     window.show()
#
#     sys.exit(app.exec_())


from PyQt5.QtWidgets import QApplication, QMainWindow
from output import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()

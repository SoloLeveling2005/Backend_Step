# # -*- coding: utf-8 -*-
# import sys
#
# ################################################################################
# ## Form generated from reading UI file 'untitled.ui'
# ##
# ## Created by: Qt User Interface Compiler version 6.3.2
# ##
# ## WARNING! All changes made in this file will be lost when recompiling UI file!
# ################################################################################
#
# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#                             QMetaObject, QObject, QPoint, QRect,
#                             QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#                            QFont, QFontDatabase, QGradient, QIcon,
#                            QImage, QKeySequence, QLinearGradient, QPainter,
#                            QPalette, QPixmap, QRadialGradient, QTransform)
# from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
#                                QStatusBar, QWidget, QLineEdit, QPushButton, QScrollArea, QVBoxLayout, QFrame, QLabel,
#                                QSpacerItem)
#
#
# class Ui_MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(QSize(700, 700))
#         self.setWindowTitle("My App")
#     def setupUi(self, QMainWindow):
#         self.centralwidget = QWidget(QMainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.lineEdit = QLineEdit(self.centralwidget)
#         self.lineEdit.setObjectName(u"lineEdit")
#         self.lineEdit.setGeometry(QRect(110, 50, 251, 20))
#         self.pushButton = QPushButton(self.centralwidget)
#         self.pushButton.setObjectName(u"pushButton")
#         self.pushButton.setGeometry(QRect(380, 50, 111, 21))
#         self.scrollArea = QScrollArea(self.centralwidget)
#         self.scrollArea.setObjectName(u"scrollArea")
#         self.scrollArea.setGeometry(QRect(110, 100, 381, 461))
#         self.scrollArea.setWidgetResizable(True)
#         self.scrollAreaWidgetContents = QWidget()
#         self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
#         self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 379, 459))
#         self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
#         self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
#         self.verticalLayoutWidget.setGeometry(QRect(10, 10, 361, 441))
#         self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
#         self.verticalLayout.setObjectName(u"verticalLayout")
#         self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.frame_2 = QFrame(self.verticalLayoutWidget)
#         self.frame_2.setObjectName(u"frame_2")
#         self.frame_2.setMinimumSize(QSize(100, 90))
#         self.frame_2.setMaximumSize(QSize(16777215, 90))
#         self.frame_2.setStyleSheet(u"border:1px solid black;")
#         self.frame_2.setFrameShape(QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QFrame.Raised)
#         self.delete_task = QPushButton(self.frame_2)
#         self.delete_task.setObjectName(u"delete_task")
#         self.delete_task.setGeometry(QRect(280, 20, 61, 51))
#         self.complate_task = QPushButton(self.frame_2)
#         self.complate_task.setObjectName(u"complate_task")
#         self.complate_task.setGeometry(QRect(210, 20, 61, 51))
#         self.label = QLabel(self.frame_2)
#         self.label.setObjectName(u"label")
#         self.label.setGeometry(QRect(10, 20, 181, 51))
#
#         self.verticalLayout.addWidget(self.frame_2)
#
#         self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
#
#         self.verticalLayout.addItem(self.verticalSpacer)
#
#         self.scrollArea.setWidget(self.scrollAreaWidgetContents)
#         MainWindow.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi(MainWindow)
#
#         QMetaObject.connectSlotsByName(MainWindow)
#         # setupUi
#
#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#         self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#         self.delete_task.setText(
#             QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
#         self.complate_task.setText(
#             QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
#         self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#     # retranslateUi
#
# app = QApplication(sys.argv)
#
# window = Ui_MainWindow()
# window.show()
#
# app.exec()

from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])
win = uic.loadUi("untitled.ui")  # расположение вашего файла .ui

win.show()
sys.exit(app.exec())

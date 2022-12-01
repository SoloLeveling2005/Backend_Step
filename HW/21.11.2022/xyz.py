# -*- coding: utf-8 -*-
import json

import requests
# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}


class Ui_MainWindow(object):
    def __init__(self):
        self.data = {"title": "Hi"}
        self.iii = 0
        self.select_tasks()



    def look1(self, idd=0):
        _translate = QtCore.QCoreApplication.translate
        if len(self.data) >= 1:
            self.frame_1 = QtWidgets.QFrame(self.verticalLayoutWidget)
            self.frame_1.setMinimumSize(QtCore.QSize(100, 60))
            self.frame_1.setMaximumSize(QtCore.QSize(16777215, 60))
            if self.data[0]['done'] is True:
                self.frame_1.setStyleSheet("border:1px solid black; background-color:green;")
            else:
                self.frame_1.setStyleSheet("border:1px solid black;")
            self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_1.setObjectName("frame_1")
            self.delete_task_1 = QtWidgets.QPushButton(self.frame_1)
            self.delete_task_1.setGeometry(QtCore.QRect(650, 10, 101, 41))
            self.delete_task_1.setObjectName("delete_task_1")
            self.delete_task_1.clicked.connect(self.delete_task_f1)

            self.complate_task_1 = QtWidgets.QPushButton(self.frame_1)
            self.complate_task_1.setGeometry(QtCore.QRect(770, 10, 101, 41))
            self.complate_task_1.setObjectName("complate_task_1")
            self.complate_task_1.clicked.connect(self.complete_task_f1)

            self.label_1 = QtWidgets.QLabel(self.frame_1)
            self.label_1.setGeometry(QtCore.QRect(10, 10, 621, 41))
            self.label_1.setStyleSheet("\n"
                                       "                                        border:0px solid black;\n"
                                       "                                    ")
            self.label_1.setObjectName("label_1")
            self.verticalLayout.addWidget(self.frame_1)
            self.delete_task_1.setText(_translate("MainWindow", "Удалить"))
            self.complate_task_1.setText(_translate("MainWindow", "Выполнить"))
            self.label_1.setText(_translate("MainWindow", f"{self.data[0]['task_title']}"))

    def look2(self, idd=1):
        _translate = QtCore.QCoreApplication.translate
        if len(self.data) >= 2:
            self.frame_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
            self.frame_2.setMinimumSize(QtCore.QSize(100, 60))
            self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
            if self.data[1]['done'] is True:
                self.frame_2.setStyleSheet("border:1px solid black; background-color:green;")
            else:
                self.frame_2.setStyleSheet("border:1px solid black;")
            self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_2.setObjectName("frame_2")
            self.delete_task_2 = QtWidgets.QPushButton(self.frame_2)
            self.delete_task_2.setGeometry(QtCore.QRect(650, 10, 101, 41))
            self.delete_task_2.setObjectName("delete_task_2")
            self.delete_task_2.clicked.connect(self.delete_task_f2)

            self.complate_task_2 = QtWidgets.QPushButton(self.frame_2)
            self.complate_task_2.setGeometry(QtCore.QRect(770, 10, 101, 41))
            self.complate_task_2.setObjectName("complate_task_2")
            self.complate_task_2.clicked.connect(self.complete_task_f2)

            self.label_2 = QtWidgets.QLabel(self.frame_2)
            self.label_2.setGeometry(QtCore.QRect(10, 10, 621, 41))
            self.label_2.setStyleSheet("\n"
                                       "                                        border:0px solid black;\n"
                                       "                                    ")
            self.label_2.setObjectName("label_2")
            self.verticalLayout.addWidget(self.frame_2)
            self.delete_task_2.setText(_translate("MainWindow", "Удалить"))
            self.complate_task_2.setText(_translate("MainWindow", "Выполнить"))
            self.label_2.setText(_translate("MainWindow", f"{self.data[1]['task_title']}"))

    def look3(self, idd=2):
        _translate = QtCore.QCoreApplication.translate
        if len(self.data) >= 3:
            self.frame_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
            self.frame_3.setMinimumSize(QtCore.QSize(100, 60))
            self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
            if self.data[2]['done'] is True:
                self.frame_3.setStyleSheet("border:1px solid black; background-color:green;")
            else:
                self.frame_3.setStyleSheet("border:1px solid black;")
            self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_3.setObjectName("frame_3")
            self.delete_task_3 = QtWidgets.QPushButton(self.frame_3)
            self.delete_task_3.setGeometry(QtCore.QRect(650, 10, 101, 41))
            self.delete_task_3.setObjectName("delete_task_3")
            self.delete_task_3.clicked.connect(self.delete_task_f3)

            self.complate_task_3 = QtWidgets.QPushButton(self.frame_3)
            self.complate_task_3.setGeometry(QtCore.QRect(770, 10, 101, 41))
            self.complate_task_3.setObjectName("complate_task_3")
            self.complate_task_3.clicked.connect(self.complete_task_f3)

            self.label_3 = QtWidgets.QLabel(self.frame_3)
            self.label_3.setGeometry(QtCore.QRect(10, 10, 621, 41))
            self.label_3.setStyleSheet("\n"
                                       "                                        border:0px solid black;\n"
                                       "                                    ")
            self.label_3.setObjectName("label_3")
            self.verticalLayout.addWidget(self.frame_3)
            self.delete_task_3.setText(_translate("MainWindow", "Удалить"))
            self.complate_task_3.setText(_translate("MainWindow", "Выполнить"))
            self.label_3.setText(_translate("MainWindow", f"{self.data[2]['task_title']}"))

    def look4(self, idd=3):
        _translate = QtCore.QCoreApplication.translate
        if len(self.data) >= 4:
            self.frame_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
            self.frame_4.setMinimumSize(QtCore.QSize(100, 60))
            self.frame_4.setMaximumSize(QtCore.QSize(16777215, 60))
            if self.data[3]['done'] is True:
                self.frame_4.setStyleSheet("border:1px solid black; background-color:green;")
            else:
                self.frame_4.setStyleSheet("border:1px solid black;")
            self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_4.setObjectName("frame_4")
            self.delete_task_4 = QtWidgets.QPushButton(self.frame_4)
            self.delete_task_4.setGeometry(QtCore.QRect(650, 10, 101, 41))
            self.delete_task_4.setObjectName("delete_task_4")
            self.delete_task_4.clicked.connect(self.delete_task_f4)

            self.complate_task_4 = QtWidgets.QPushButton(self.frame_4)
            self.complate_task_4.setGeometry(QtCore.QRect(770, 10, 101, 41))
            self.complate_task_4.setObjectName("complate_task_4")
            self.complate_task_4.clicked.connect(self.complete_task_f4)

            self.label_4 = QtWidgets.QLabel(self.frame_4)
            self.label_4.setGeometry(QtCore.QRect(10, 10, 621, 41))
            self.label_4.setStyleSheet("\n"
                                       "                                        border:0px solid black;\n"
                                       "                                    ")
            self.label_4.setObjectName("label_4")
            self.verticalLayout.addWidget(self.frame_4)
            self.delete_task_4.setText(_translate("MainWindow", "Удалить"))
            self.complate_task_4.setText(_translate("MainWindow", "Выполнить"))
            self.label_4.setText(_translate("MainWindow", f"{self.data[3]['task_title']}"))

    def look5(self, idd=4):
        _translate = QtCore.QCoreApplication.translate
        if len(self.data) >= 5:
            self.frame_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
            self.frame_5.setMinimumSize(QtCore.QSize(100, 60))
            self.frame_5.setMaximumSize(QtCore.QSize(16777215, 60))
            if self.data[4]['done'] is True:
                self.frame_5.setStyleSheet("border:1px solid black; background-color:green;")
            else:
                self.frame_5.setStyleSheet("border:1px solid black;")
            self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_5.setObjectName("frame_5")
            self.delete_task_5 = QtWidgets.QPushButton(self.frame_5)
            self.delete_task_5.setGeometry(QtCore.QRect(650, 10, 101, 41))
            self.delete_task_5.setObjectName("delete_task_5")
            self.delete_task_5.clicked.connect(self.delete_task_f5)

            self.complate_task_5 = QtWidgets.QPushButton(self.frame_5)
            self.complate_task_5.setGeometry(QtCore.QRect(770, 10, 101, 41))
            self.complate_task_5.setObjectName("complate_task_5")
            self.complate_task_5.clicked.connect(self.complete_task_f5)

            self.label_5 = QtWidgets.QLabel(self.frame_5)
            self.label_5.setGeometry(QtCore.QRect(10, 10, 621, 41))
            self.label_5.setStyleSheet("\n"
                                       "                                        border:0px solid black;\n"
                                       "                                    ")
            self.label_5.setObjectName("label_5")
            self.verticalLayout.addWidget(self.frame_5)
            self.delete_task_5.setText(_translate("MainWindow", "Удалить"))
            self.complate_task_5.setText(_translate("MainWindow", "Выполнить"))
            self.label_5.setText(_translate("MainWindow", f"{self.data[4]['task_title']}"))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1257, 1211)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 50, 771, 55))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("\n"
                                    "                    padding:40px 10px; \n"
                                    "                    border:1px solid black;\n"
                                    "                ")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 50, 101, 55))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
                                      "                    background-color:white;\n"
                                      "                    border:1px solid black;\n"
                                      "                ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.create_task)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 130, 900, 471))
        self.scrollArea.setStyleSheet("\n"
                                      "                    border:0px solid black;\n"
                                      "                ")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 900, 471))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 890, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.look1()
        self.look2()
        self.look3()
        self.look4()
        self.look5()

        # spacerItem = QtWidgets.QSpacerItem(356, 372, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo"))
        self.pushButton.setText(_translate("MainWindow", "Создать"))


    def delete_and_look(self, val=None):
        self.select_tasks()
        try:
            self.frame_1.setParent(None)
        except:
            pass
        try:
            self.frame_2.setParent(None)
        except:
            pass
        try:
            self.frame_3.setParent(None)
        except:
            pass
        try:
            self.frame_4.setParent(None)
        except:
            pass
        try:
            self.frame_5.setParent(None)
        except:
            pass

        self.look1()
        self.look2()
        self.look3()
        self.look4()
        self.look5()
        # if val is None:
        #     pass
        # elif val == 0:
        #     self.frame_1.setStyleSheet("border:1px solid black; background-color:green;")
        # elif val == 1:
        #     self.frame_2.setStyleSheet("border:1px solid black; background-color:green;")
        # elif val == 2:
        #     self.frame_3.setStyleSheet("border:1px solid black; background-color:green;")
        # elif val == 3:
        #     self.frame_4.setStyleSheet("border:1px solid black; background-color:green;")
        # elif val == 4:
        #     self.frame_5.setStyleSheet("border:1px solid black; background-color:green;")
        # elif val == 5:
        #     self.frame_6.setStyleSheet("border:1px solid black; background-color:green;")
    def delete_task_f1(self):
        id_task = self.data[0]['id']
        response = requests.get(
            url=f"http://127.0.0.1:8000/todo_app/delete_task/{id_task}",
            headers=headers
        )
        data = response.text
        print(json.loads(response.text)['response'])

        self.delete_and_look()
        print("delete_task1")

    def delete_task_f2(self):
        id_task = self.data[1]['id']
        response = requests.get(
            url=f"http://127.0.0.1:8000/todo_app/delete_task/{id_task}",
            headers=headers
        )
        data = response.text
        print(json.loads(response.text)['response'])
        self.delete_and_look()
        print("delete_task2")

    def delete_task_f3(self):
        id_task = self.data[2]['id']
        response = requests.get(
            url=f"http://127.0.0.1:8000/todo_app/delete_task/{id_task}",
            headers=headers
        )
        data = response.text
        print(json.loads(response.text)['response'])
        self.delete_and_look()
        print("delete_task3")

    def delete_task_f4(self):
        id_task = self.data[3]['id']
        response = requests.get(
            url=f"http://127.0.0.1:8000/todo_app/delete_task/{id_task}",
            headers=headers
        )
        data = response.text
        print(json.loads(response.text)['response'])
        self.delete_and_look()
        print("delete_task4")

    def delete_task_f5(self):
        id_task = self.data[4]['id']
        response = requests.get(
            url=f"http://127.0.0.1:8000/todo_app/delete_task/{id_task}",
            headers=headers
        )
        data = response.text
        print(json.loads(response.text)['response'])
        self.delete_and_look()
        print("delete_task5")

    def complete_task_f1(self):
        id_task = self.data[0]['id']
        response = requests.get(
            url=f"http://127.0.0.1:8000/todo_app/complete_task/{id_task}",
            headers=headers
        )
        data = response.text
        print(json.loads(response.text)['response'])
        self.delete_and_look()
        print("complete_task1")

    def complete_task_f2(self):
        id_task = self.data[1]['id']
        response = requests.get(
            url=f"http://127.0.0.1:8000/todo_app/complete_task/{id_task}",
            headers=headers
        )
        data = response.text
        print(json.loads(response.text)['response'])
        self.delete_and_look()
        print("complete_task2")

    def complete_task_f3(self):
        id_task = self.data[2]['id']
        response = requests.get(
            url=f"http://127.0.0.1:8000/todo_app/complete_task/{id_task}",
            headers=headers
        )
        data = response.text
        print(json.loads(response.text)['response'])
        self.delete_and_look()
        print("complete_task3")

    def complete_task_f4(self):
        id_task = self.data[3]['id']
        response = requests.get(
            url=f"http://127.0.0.1:8000/todo_app/complete_task/{id_task}",
            headers=headers
        )
        data = response.text
        print(json.loads(response.text)['response'])
        self.delete_and_look()
        print("complete_task4")

    def complete_task_f5(self):
        id_task = self.data[4]['id']
        response = requests.get(
            url=f"http://127.0.0.1:8000/todo_app/complete_task/{id_task}",
            headers=headers
        )
        data = response.text
        print(json.loads(response.text)['response'])
        self.delete_and_look()
        print("complete_task5")

    def select_tasks(self):
        response = requests.get(
            url="http://127.0.0.1:8000/todo_app/get_tasks/",
            headers=headers
        )
        # data = json.loads(response.content)
        # self.data = data
        print("select_tasks")
        data = response.text
        print(data)
        print(json.loads(response.text)['response'])
        self.data = json.loads(response.text)['response']

    def create_task(self):
        print("create_task")
        try:
            print(f"http://127.0.0.1:8000/todo_app/create_task/{self.lineEdit.text()}")
            response = requests.post(
                url=f"http://127.0.0.1:8000/todo_app/create_task/{self.lineEdit.text()}",
                data=self.lineEdit.text(),
                headers=headers
            )
            self.lineEdit.setText("")
            print(response)
            self.select_tasks()
            if len(self.data) == 1:
                self.look1()
            elif len(self.data) == 2:
                self.look2()
            elif len(self.data) == 3:
                self.look3()
            elif len(self.data) == 4:
                self.look4()
            elif len(self.data) == 5:
                self.look5()

        except Exception as e:
            print(e)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # + тут ваша логика


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    p = MainWindow()
    p.show()
    sys.exit(app.exec_())

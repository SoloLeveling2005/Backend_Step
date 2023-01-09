import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QRadioButton
from PyQt6.QtCore import Qt





class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.update_true_or_false = ""
        self.host = "http://192.168.0.38:8000/"
        self.setWindowTitle('App')

        # set the grid layout
        layout = QGridLayout()
        self.setLayout(layout)


        # GET all data
        layout.addWidget(QLabel('Получить все данные'), 0, 0)

        self.button_get_all_data = QPushButton('Получить')
        self.button_get_all_data.clicked.connect(self.func_get_all_data)
        layout.addWidget(self.button_get_all_data, 1, 0)


        # GET data by id
        layout.addWidget(QLabel('Получить выборочные данные по userId'), 0, 1)

        self.userId_get = QLineEdit()
        self.userId_get.setPlaceholderText("* Введите userId") 
        layout.addWidget(self.userId_get, 1, 1)

        self.button_get_data_by_id = QPushButton('Получить')
        self.button_get_data_by_id.clicked.connect(self.func_get_data_by_id)
        layout.addWidget(self.button_get_data_by_id, 2, 1)


        # DELETE data by id
        layout.addWidget(QLabel('Удалить выборочные данные по id'), 0, 2)
        self.id_delete = QLineEdit()
        self.id_delete.setPlaceholderText("* Введите id") 
        layout.addWidget(self.id_delete, 1, 2)
        layout.addWidget(QPushButton('Не работает'), 2, 2)


        # UPDATE data by id
        layout.addWidget(QLabel('Обновить данные'), 0, 3)
        self.id_update = QLineEdit()
        self.id_update.setPlaceholderText("* Введите id") 
        layout.addWidget(self.id_update, 1, 3)

        self.title_update = QLineEdit()
        self.title_update.setPlaceholderText("Введите title") 
        layout.addWidget(self.title_update, 2, 3)
        
        self.check1_update = QRadioButton("True", self)
        self.check1_update.clicked.connect(self.showDetails)
        layout.addWidget(self.check1_update, 3, 3)
 
        self.check2_update = QRadioButton("False", self)
        self.check2_update.clicked.connect(self.showDetails)
        layout.addWidget(self.check2_update, 3, 3, alignment=Qt.AlignmentFlag.AlignRight)
        # layout.addWidget(QPushButton('Обновить'), 4, 3)

        self.button_update_data = QPushButton('Не работает')
        # self.button_update_data.clicked.connect(self.func_update_data_by_id)
        layout.addWidget(self.button_update_data, 4, 3)


        # POST data by id
        layout.addWidget(QLabel('Добавить данные'), 0, 4)
        self.title_post = QLineEdit()
        self.title_post.setPlaceholderText("* Введите title") 
        layout.addWidget(self.title_post, 1, 4)

        self.check1_post = QRadioButton("True", self)
        self.check1_post.clicked.connect(self.showDetails)
        layout.addWidget(self.check1_post, 2, 4)
 
        self.check2_post = QRadioButton("False", self)
        self.check2_post.clicked.connect(self.showDetails)
        layout.addWidget(self.check2_post, 2, 4, alignment=Qt.AlignmentFlag.AlignRight)

        self.button_post_data = QPushButton('Создать')
        self.button_post_data.clicked.connect(self.func_post_data_by_id)
        layout.addWidget(self.button_post_data, 3, 4)
      
    
        self.message = QLabel('Сообщений нет')
        self.message.setWordWrap(True)
        # self.id_update.setPlaceholderText("* Введите id") 
        layout.addWidget(self.message, 5, 0)


        # show the window
        self.show()


    def showDetails(self):
        print("Name:", self.sender().text())
        self.update_true_or_false = self.sender().text()

    def func_get_all_data(self):
        response = requests.get(url=f"{self.host}api/posts/")
        data = response.json()
        print(data, type(data))
        self.message.setText(str(data))

    def func_get_data_by_id(self):
        # print(self.userId_get.text())
        if (self.userId_get.text() == ''):
            pass
        else:
            try:
                response = requests.get(url=f"{self.host}api/posts/{self.userId_get.text()}/")
                data = response.json()
                print(data, type(data))
                self.message.setText(str(data))
            except Exception as e:
                print(e)
                self.message.setText("Данных нет")

    # def func_update_data_by_id(self):
    #     print(self.userId_get.text())
    #     if (self.id_update.text() == ''):
    #         pass
    #     else:
    #         try:
    #             params = {}
    #             if self.title_update.text() != "":
    #                 params['title'] = self.title_update.text()

    #             if self.update_true_or_false == 'False':
    #                 params['completed'] = False
    #             elif self.update_true_or_false == 'True':
    #                 params['completed'] = True

    #             response = requests.put(url=f"http://127.0.0.1:8000/api/posts/{self.id_update.text()}", data=params)
    #             data = response.json()
    #             print(data, type(data))
    #         except Exception as e:
    #             print(e)

    def func_post_data_by_id(self):
        if (self.title_post.text() == ''):
            pass
        else:
            try:
                params = {}
                params['title'] = self.title_post.text()
                if self.update_true_or_false == 'False':
                    params['completed'] = False
                elif self.update_true_or_false == 'True':
                    params['completed'] = True
                response = requests.post(url=f"{self.host}api/posts/", json = params)
                data = response.json()
                print(data, type(data))
                self.message.setText(str(data))
            except Exception as e:
                print(e)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

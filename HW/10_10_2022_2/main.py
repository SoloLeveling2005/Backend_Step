import argparse
import os
import sys

import psycopg2 as psycopg2
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit
from werkzeug.utils import secure_filename
import cv2
connect = "dbname='postgres' user='postgres' host='localhost' password='Solo2005'"
connection = psycopg2.connect(connect)
cursor = connection.cursor()


def connect_def(connect):
    global connection
    global cursor
    connection = psycopg2.connect(connect)
    cursor = connection.cursor()
connect_def(connect)

# connect_def(connect)
# cursor.execute(f"""
#             INSERT INTO public."user"(
#             login, password)
#             VALUES ('123', '123');""")
# cursor.close()
#
# connection.commit()
# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        super(MainWindow, self).__init__()
        self.setWindowTitle("Добавлени и возрат с БД")


        layout = QVBoxLayout()

        # Устанавливаем центральный виджет Window.
        self.input_url = QLineEdit()
        self.input_url.setPlaceholderText("Введите название фото в данной дерриктории")

        button = QPushButton("Преобразовать")
        button.clicked.connect(self.do)


        button.setStyleSheet(
            "QPushButton { padding: 5px 7px; text-align: center; }"
        )

        layout.addWidget(button)
        layout.addWidget(self.input_url)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    def do(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", required=True, help="path to input image")
        args = vars(ap.parse_args())
        file = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
        path = self.input_url.text()
        UPLOAD_FOLDER = self.input_url.text()
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        img = cv2.imread(f'{path}/{filename}')
        # Scale down to 30%
        p = 0.30
        w = int(img.shape[1] * p)
        h = int(img.shape[0] * p)
        new_img = cv2.resize(img, (w, h))
        cv2.imwrite(f'{path}/{filename}', new_img)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
window.setFixedSize(600,500)
app.exec()


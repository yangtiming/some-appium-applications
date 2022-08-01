import threading
import os
import time


def press_():
    while True:
        for i in range(300000):
            os.system('adb shell input tap 210 480')

def main():

    for i in range(5):
      press = threading.Thread(target=press_)
      press.start()



if __name__ == '__main__':
    main()

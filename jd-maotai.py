import requests
import datetime
import os
import random
import time
import multiprocessing
import threading
def TM_time():
  class Jingdongtime(object):
    r1 = requests.get(url='https://api.m.jd.com/client.action?functionId=queryMaterialProducts&client=wh5',
                      headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'})

    x = eval(r1.text)
    timeNum = int(x['currentTime2'])

    def funcname():
      timeStamp = float(Jingdongtime.timeNum) / 1000
      ret_datetime = datetime.datetime.fromtimestamp(timeStamp).strftime("%Y-%m-%d %H:%M:%S.%f")
      return ret_datetime,Jingdongtime.timeNum

  t,time_t = Jingdongtime.funcname()
  return t[10:],time_t


def diff(diff):
    timeStamp = float(diff) / 1000
    ret_datetime = datetime.datetime.fromtimestamp(timeStamp).strftime("%Y-%m-%d %H:%M:%S.%f")
    return ret_datetime

def press_():
  while True:
    os.system('adb shell input tap 900 1850')
def press__():
  while True:
    time.sleep(10)
    os.system('adb shell input tap 90 150')
def main():

    for i in range(6):
      press = threading.Thread(target=press_)
      press.start()
    press = threading.Thread(target=press__)
    press.start()

if __name__ == '__main__':
    time_t=""
    TM_times,time_t = TM_time()
    flag = 0
    data = "2022-07-18 12:00:00"
    #data = "2022-07-12 16:38:00"
    timeArray = time.strptime(data, "%Y-%m-%d %H:%M:%S")
    times_data = int(time.mktime(timeArray)*1000)
    pc_t = int(time.time() * 1000)
    TM_DIFF= (time_t-pc_t)
    while True:
        pc_t = int(time.time()*1000)
        wait_time = times_data - (pc_t+TM_DIFF)

        if wait_time <  2000 :
            print("OK")
            flag = 1
            break
    if flag ==1 :
        main()

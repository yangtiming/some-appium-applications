import threading

import requests
import datetime
import os
import random
import time
import multiprocessing

def TM_time():
  class Jingdongtime(object):
    r1 = requests.get(url='http://api.m.taobao.com/rest/api3.do?api=mtop.common.gettimestamp',
                      headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'})

    x = eval(r1.text)
    timeNum = int(x['data']['t'])

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
        os.system('adb shell input tap 900 1840')
        #os.system('adb shell input tap 560 1840')
def press__():
    os.system('adb shell input tap 860 1700')
def main(pc_t):
    press_all=[]
    for i in range(5):
      press_all.append(threading.Thread(target=press_))

    for i in range(len(press_all)):
      press_all[i].start()
      print(int(time.time() * 1000) - pc_t)

if __name__ == '__main__':
    time_t=""
    TM_times,time_t = TM_time()
    flag = 0
    data = "2022-07-19 20:00:00"
    #data = "2022-07-12 16:38:00"
    timeArray = time.strptime(data, "%Y-%m-%d %H:%M:%S")
    times_data = int(time.mktime(timeArray)*1000)
    pc_t = int(time.time() * 1000)
    TM_DIFF= (time_t-pc_t)
    press_0 = threading.Thread(target=press__)
    while True:
        pc_t = int(time.time()*1000)
        wait_time = times_data - (pc_t+TM_DIFF)

        if wait_time < 700+50:
            print(wait_time, TM_DIFF)
            print("OK")
            flag = 1
            break
    if flag ==1 :
        #press_0.start()
        os.system('adb shell input tap 860 1700')
        print("FIRST",int(time.time() * 1000) - pc_t)
        main(pc_t)


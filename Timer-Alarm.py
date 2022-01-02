#!/usr/bin/env python3
import time
from pygame import mixer


def alarm():
    mixer.init()
    mixer.music.load('alarm.mp3')
    mixer.music.play()
    while mixer.music.get_busy() == True:
        if input() != '': mixer.music.stop()
        continue
    mixer.quit()


try:
    work_interval = float(input('Work time interval (minutes): '))
    rest_interval = float(input('Rest time interval (minutes): '))
except:
    print('ERROR! Invalid input format\n'
          'Standard parameters selected')
    work_interval = 50
    rest_interval = 10

while True:
    time.sleep(work_interval * 60)
    alarm()
    time.sleep(rest_interval * 60)
    alarm()

import asyncio
from pygame import mixer


def alarm():
    mixer.init()
    mixer.music.load('alarm.mp3')
    mixer.music.play()
    while mixer.music.get_busy() == True:
        if input() != '': mixer.music.stop()
        continue
    mixer.quit()

async def main(work_interval, rest_interval):
    while True:
        await asyncio.sleep(work_interval * 60)
        alarm()
        await asyncio.sleep(rest_interval * 60)
        alarm()

try:
    work_interval = float(input('Work time interval (minutes): '))
    rest_interval = float(input('Rest time interval (minutes): '))
except:
    print('ERROR! Invalid input format\n'
          'Standard parameters selected')
    work_interval = 50
    rest_interval = 10

asyncio.run(main(work_interval, rest_interval))
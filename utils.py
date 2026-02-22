import time
import os

def timeCls(timer, clear):
    time.sleep(timer)
    if clear == 'cls':
        os.system('cls')
    pass
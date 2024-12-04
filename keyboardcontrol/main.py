import random
import pyautogui as pg
import time
from _datetime import datetime

b = ('bassin', 'besen', 'yasin')

for i in range(50):
    a = random.choice(b)
    now = datetime.now()
    c = str(now.strftime("%H:%M:%S"))
    pg.write('es ist: ' + c)
    pg.press('enter')
    time.sleep(0)


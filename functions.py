
import pydirectinput as p
import time as t
from python_imagesearch.imagesearch import imagesearch_from_folder


monkeys = {'hero':'u',
'dart':'q','boomerang':'w','bomb':'e','tack':'r','ice':'t','glue':'y',
'sniper':'z','sub':'x','buccaneer':'c','ace':'v','heli':'b','mortar':'n..x','dartling':'m',
'wizard':'a','super':'s','ninja':'d','alchemist':'f','druid':'g',
'spac':'j','village':'k','engineer':'l'}

def startgame():
    p.click(960, 540)
    p.press('enter', interval=0.25)
    p.press('space', presses=2, interval=0.25)

def restartgame():
    t.sleep(1)
    p.press('enter', interval=0.25)
    t.sleep(1)  
    p.press('escape')
    p.click(1070, 840, interval=0.25)
    p.click(1130, 725, interval=0.25)

def checknotif():
    while True:
        t.sleep(2)
        imgs=imagesearch_from_folder('./', 0.8)
        try:
            if imgs['./win.png'] != [-1, -1]:
                t.sleep(1)
                p.click(960,910)
                t.sleep(1)
                p.click(1230, 840)
                break
            elif imgs['./levelup.png'] != [-1, -1]:
                t.sleep(1)
                p.click(960, 540)
                t.sleep(1)
                p.click(960, 540)
                t.sleep(1)
                p.press('space', presses=2, interval=0.25)
                pass
            else:
                pass
        except:
            pass

def build(monkey, x, y, upgr, t=0):
    p.press(monkeys[monkey])
    p.moveTo(x, y)
    p.doubleClick(interval=0.1)
    upgrades = ','*int(upgr[0]) + '.'*int(upgr[1]) + '/'*int(upgr[2])
    p.write(upgrades)
    p.press('tab', presses=t, interval=0.1)
    p.press('escape')

def sell(x, y):
    p.click(x,y, interval=0.1)
    t.sleep(0.1)
    p.press('backspace')

def upgrade(x, y, upgr):
    p.click(x, y)
    t.sleep(0.2)
    upgrades = ','*int(upgr[0]) + '.'*int(upgr[1]) + '/'*int(upgr[2])
    p.write(upgrades)
    p.click(960,540)

#t.sleep(5)
#print(p.position())

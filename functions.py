import pydirectinput as p
import pyautogui as s
import time as t
import os
from pathlib import Path
from tkinter import *


monkeys = {'hero':'u',
'dart':'q','boomerang':'w','bomb':'e','tack':'r','ice':'t','glue':'y',
'sniper':'z','sub':'x','buccaneer':'c','ace':'v','heli':'b','mortar':'n','dartling':'m',
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
        t.sleep(1)
        if s.locateOnScreen('win.png', confidence=0.8) != None:
            t.sleep(1)
            p.click(960,910)
            t.sleep(1)
            p.click(1230, 840)
            break
        elif s.locateOnScreen('levelup.png', confidence=0.8) != None:
            t.sleep(1)
            p.click(960, 540)
            t.sleep(1)
            p.click(960, 540)
            t.sleep(1)
            p.press('space', presses=2, interval=0.25)
            pass
        else:
            pass

def build(monkey, x, y, upgr, t=0):
    p.press(monkeys[monkey])
    p.moveTo(x, y)
    p.doubleClick(interval=0.1)
    upgrades = ','*int(upgr[0]) + '.'*int(upgr[1]) + '/'*int(upgr[2])
    p.write(upgrades, interval=0.01)
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
    p.write(upgrades, interval=0.01)
    p.click(960,540)

def filebuild(map, gamemode, strategy):
    folder = Path("maps/%s/%s/" %(map, gamemode))
    file = folder / strategy
    with open(file, 'r') as lines:
        for line in lines:
            exec(line)

#t.sleep(5)
#print(p.position())

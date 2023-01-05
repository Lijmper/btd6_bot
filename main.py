import pydirectinput as p
import pyautogui as s
import time as t
import tkinter as tk
import os
import threading
import sys
from pathlib import Path

p.FAILSAFE = True
stop_event = threading.Event()

monkeys = {'hero':'u',
'dart':'q','boomerang':'w','bomb':'e','tack':'r','ice':'t','glue':'y',
'sniper':'z','sub':'x','buccaneer':'c','ace':'v','heli':'b','mortar':'n','dartling':'m',
'wizard':'a','super':'s','ninja':'d','alchemist':'f','druid':'g',
'spac':'j','village':'k','engineer':'l'}

mapcodes = {'Dark Castle':'dc','Infernal':'in'}
modecodes = {'Deflation':'de'}
stratcodes = {'Obyn Super':'os','Jones Bomb':'jb'}

maps = ["Dark Castle"]
modes = ["Deflation"]
strats = ["Obyn Super", "Jones Bomb"]

stratspath = Path("strats")
imagespath = Path("images")

def show():
    plan.config(text=("%s - %s - %s" %(map.get(), mode.get(), strat.get())))

def stop():
    global stop_event
    stop_event.set()
    mainrunthread.join()
    runbutton["state"] = "active"

def map_selected(value):
    map.set(value)
    show()

def mode_selected(value):
    mode.set(value)
    show()

def strat_selected(value):
    strat.set(value)
    show()

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

def waiting(starttime, gamecount):
    wait = True
    average = 0.0
    global stop_event
    while wait == True and not stop_event.is_set():
        t.sleep(0.01)
        if s.locateOnScreen(str(imagespath / 'win.png'), confidence=0.8) != None:
            t.sleep(1)
            p.click(960,910)
            t.sleep(1)
            p.click(1230, 840)
            gamecount += 1
            average = total/gamecount
            wait = False
        elif s.locateOnScreen(str(imagespath / 'levelup.png'), confidence=0.8) != None:
            t.sleep(1)
            p.click(960, 540)
            t.sleep(1)
            p.click(960, 540)
            t.sleep(1)
            p.press('space', presses=2, interval=0.25)
        stop = t.time()
        total = stop-starttime
        seconds = int(total%60)
        minutes = int((total%3600)/60)
        hours = int(total/3600)
        progressionstring = 'Game %d, MM earned: %d, time: %s:%s.%s, avg: %.1f sec' %(gamecount, gamecount*66, str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2), average)
        progress.config(text=progressionstring)
        if stop_event.is_set():
            progress.config(text="Waiting for game")

def build(monkey, x, y, upgr, t=0):
    p.press(monkeys[monkey])
    p.moveTo(x, y)
    p.doubleClick(interval=0.1)
    upgrades = ','*int(upgr[0]) + '.'*int(upgr[1]) + '/'*int(upgr[2])
    p.write(upgrades, interval=0.01)
    p.press('tab', presses=t, interval=0.1)
    p.press('escape')
    pass

def sell(x, y):
    p.click(x,y, interval=0.1)
    t.sleep(0.1)
    p.press('backspace')
    pass

def upgrade(x, y, upgr):
    p.click(x, y)
    t.sleep(0.2)
    upgrades = ','*int(upgr[0]) + '.'*int(upgr[1]) + '/'*int(upgr[2])
    p.write(upgrades, interval=0.01)
    p.click(960,540)
    pass

def filebuild(map, gamemode, strategy):
    filename = '%s_%s_%s.txt' %(mapcodes[map], modecodes[gamemode], stratcodes[strategy])
    file = stratspath / filename
    with open(file, 'r') as lines:
        for line in lines:
            exec(line)

def script(map, mode, strat):
    starttime = t.time()
    gamecount = 0
    while True and (not stop_event.is_set()):
        t.sleep(1)
        p.click(960, 540)
        filebuild(map, mode, strat)
        startgame()
        waiting(starttime, gamecount)
        if stop_event.is_set():
            progress.config(text="Waiting for game")
            break
        restartgame()

def mainrun(stop_event):
    if map.get() != 'Maps':
        if mode.get() != 'Gamemode':
            if strat.get() != 'Strategy':
                runbutton["state"] = "disabled"
                currentmap = map.get()
                currentmode = mode.get()
                currentstrat = strat.get()
                progress.config(text='Game 0, MM earned: 0, time: 00:00.00, avg 0.0 sec')
                stop_event.clear()
                script(currentmap, currentmode, currentstrat)
            else:
                plan.config(text=("Missing argument"))
        else:
            plan.config(text=("Missing argument"))
    else:
        plan.config(text=("Missing argument"))

mainrunthread = threading.Thread(target=mainrun, args=[stop_event])
mainrunthread.setDaemon(True)

window = tk.Tk()

window.geometry("310x100")
window.resizable(False, False)
window.wm_title("limpi BTD6 bot")
window.iconbitmap(imagespath / 'robomonkey.ico')

map = tk.StringVar()
map.set("Maps")
mode = tk.StringVar()
mode.set("Gamemode")
strat = tk.StringVar()
strat.set("Strategy")

plan = tk.Label(window, text=("%s - %s - %s" %(map.get(), mode.get(), strat.get())))
plan.place(x=75, y=40, height=30, )

progress = tk.Label(window, text="Waiting for game")
progress.place(x=5, y=75, height=30, )

runbutton = tk.Button(text='Run', command=mainrunthread.start)
runbutton.place(x=5, y=40, height=30)

stopbutton = tk.Button(text='Stop', command=stop)
stopbutton.place(x=40, y=40, height=30)

dropmaps = tk.OptionMenu(window, map, *maps, command=map_selected)
dropmaps.place(x=5, y=5, width=100, height=30)

dropmode = tk.OptionMenu(window, mode, *modes, command=mode_selected)
dropmode.place(x=105, y=5, width=100, height=30)

dropstrat = tk.OptionMenu(window, strat, *strats, command=strat_selected)
dropstrat.place(x=205, y=5, width=100, height=30)

window.mainloop()

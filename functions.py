import functions as btd6
from functions import *
p.FAILSAFE= True

# main = Tk()

# main.geometry("250x300")

# maps = ["Dark Castle", "Infernal"]
# gamemode = ["Deflation"]
# strat = ["Obyn Super", "Jones Bomb"]

# clickmaps = StringVar()
# clickmaps.set("Maps")
# clickmode = StringVar()
# clickmode.set("Gamemode")
# clickstrat = StringVar()
# clickstrat.set("Strategy")

# dropmaps = OptionMenu(main, clickmaps, *maps).pack()
# dropmode = OptionMenu(main, clickmode, *gamemode)
# dropmode.pack()
# dropstrat = OptionMenu(main, clickstrat, *strat)
# dropstrat.pack()

# main.mainloop()

t.sleep(3)
gamecount = 0
monkeymoney = 0
start = t.time()

map = 'darkcastle'
gamemode = 'deflation'
strategy = 'obyn_super.txt' #obyn_super.txt or jones_bomb.txt

while True:
    gamecount += 1
    monkeymoney += 60

    p.click(960, 540)
    btd6.filebuild(map, gamemode, strategy)
    btd6.startgame()
    btd6.checknotif()
    stop = t.time()
    btd6.restartgame()
    total = stop-start
    seconds = int(total%60)
    minutes = int((total%3600)/60)
    hours = int(total/3600)
    print('Game %d, MM earned: %d, total time: %s:%s.%s, average time: %.1f seconds' %(gamecount, monkeymoney, str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2), (stop-start)/gamecount))
    # break

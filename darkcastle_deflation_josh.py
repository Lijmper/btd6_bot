import pydirectinput as p
import time as t
import functions as btd6
p.FAILSAFE= True

gamecount = 0
t.sleep(3)
monkeymoney = 0

while True:
    start = t.time()
    gamecount += 1
    monkeymoney += 60

    btd6.build('village', 846, 292, '002')
    btd6.build('bomb', 697, 425, '420')
    btd6.build('bomb', 773, 424, '230')
    btd6.build('bomb', 849, 429, '204')
    btd6.build('bomb', 667, 348, '130')
    btd6.build('bomb', 660, 279, '130')
    btd6.build('hero', 761, 357, '000')
    btd6.sell(846, 292)
    btd6.build('village', 846, 292, '020')

    btd6.startgame()
    p.click(960, 540)
    btd6.checknotif()
    btd6.restartgame()
    stop = t.time()
    print('Game %s, time taken: %s seconds, MM earned: %s' %(gamecount, int(stop-start), monkeymoney))

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

    btd6.build('village', 830, 294, '002')
    btd6.build('bomb', 707, 429, '420')
    btd6.build('bomb', 887, 427, '230')
    btd6.build('bomb', 863, 427, '204')
    btd6.build('bomb', 684, 364, '130')
    btd6.build('bomb', 666, 269, '130')
    btd6.build('hero', 762, 364, '200')
    btd6.sell(830, 294)
    btd6.build('village', 830, 294, '020')

    btd6.startgame()
    p.click(960, 540)
    btd6.checknotif()
    btd6.restartgame()
    stop = t.time()
    print('Game %s, time taken: %s seconds, MM earned: %s' %(gamecount, int(stop-start), monkeymoney))
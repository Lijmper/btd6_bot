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
    btd6.build('village', 740, 327, '002')
    btd6.build('village', 854, 275, '002')
    btd6.build('village', 966, 354, '002')
    btd6.build('super', 761, 429, '203')
    btd6.build('ninja', 853, 440, '302')
    btd6.build('alchemist', 929, 440, '301')
    btd6.sell(740, 327)
    btd6.sell(854, 275)
    btd6.sell(966,354)
    btd6.upgrade(853, 440, '100')
    btd6.build('hero', 851, 379, '200')
    btd6.startgame()
    p.click(960, 540)
    btd6.checknotif()
    btd6.restartgame()
    stop = t.time()
    print('Game %s, time taken: %s seconds, MM earned: %s' %(gamecount, int(stop-start), monkeymoney))
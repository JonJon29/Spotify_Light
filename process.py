import json
import time
import board
import neopixel

pixelsL = neopixel.NeoPixel(board.D18, 72)
pixelsR = neopixel.NeoPixel(board.D23, 72)

pixelsL.auto_write = False
pixelsR.auto_write = False

with open('testData.json') as file:
    data = json.load(file)

lenth = len(data['left'])

for x in range(0, lenth):
    x = str(x)
    wertL = (data['left'][x])
    gesamtL = wertL.split('.')
    rL = int(gesamtL[0])
    gL = int(gesamtL[1])
    bL = int(gesamtL[2])
    for v in range(0,72):
        pixelsL[v] = (rL, gL, bL)
        pixelsL.show()
        
    wertR = (data['right'][x])
    gesamtR = wertR.split('.')
    rR = int(gesamtR[0])
    gR = int(gesamtR[1])
    bR = int(gesamtR[2])
    for v in range(0, 72):
        pixelsR[v] = (rR, gR, bR)
        pixelsR.show()

    wertS = (data['strobo'][x])
    #print(rL, + gL + bL)
    #print(rR + gR + bR)
    #print(wertS)
    time.sleep(2)
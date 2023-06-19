import json
import time
import board
import neopixel
import RPi.GPIO as GPIO

pixelsL = neopixel.NeoPixel(board.D18, 72)
pixelsR = neopixel.NeoPixel(board.D16, 72)

pixelsL.auto_write = False
pixelsR.auto_write = False

with open('testData.json') as file:
    data = json.load(file)

lenth = len(data['left'])

mospfet_pin = 13
led_pin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(mospfet_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 50)

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
    if wertS == "on":
        strobo()
    time.sleep(2)

    def strobo():
        GPIO.output(mospfet_pin, GPIO.HIGH)
        pwm.start(50)
        time.sleep(1)
        pwm.stop()
        GPIO.output(mospfet_pin, GPIO.LOW)
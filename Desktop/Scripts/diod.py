import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

for i in range (0, 10):
    GPIO.output(26, 1)
    time.sleep(0.5)
    
    GPIO.output(26, 0)
    time.sleep(0.5)

GPIO.cleanup()
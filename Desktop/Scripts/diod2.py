import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

GPIO.output(26, GPIO.input(23))
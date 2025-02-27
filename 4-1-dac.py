import RPi.GPIO as GPIO
def dec2bin(decnum):
    if decnum == 0:
        return [0, 0, 0, 0, 0, 0, 0, 0]

    bins = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while decnum > 0:
        bins[i] = decnum % 2
        decnum = decnum // 2
        i = i + 1

    bins.reverse()

    return bins

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        n = input("Введите число:")
        try:
            n = int(n)
            if 0 <= n <= 255:
                GPIO.output(dac, dec2bin(n))
                print(dec2bin(n))
                volt = float(n) / 256.0 * 3.3
                print("Вольт:", volt)
            else:
                if (n < 0) or (n > 255):
                    print("Error")
        except Exception:
            if n == "q": break




finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

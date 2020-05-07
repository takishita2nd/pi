import time
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

while True:
    temp = int(sense.get_temperature())
    print(temp)
    y = temp // 8
    x = temp % 8
    for dy in range(0, y + 1):
        if dy < y:
            for dx in range(0, 8):
                sense.set_pixel(dx, dy, 255, 0, 0)
        else:
            for dx in range(0, 8):
                sense.set_pixel(dx, dy, 0, 0, 0)
            for dx in range(0, x):
                sense.set_pixel(dx, dy, 255, 0, 0)
    #time.sleep(1)

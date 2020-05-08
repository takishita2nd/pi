from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

x, y = 0, 0
clear = [0, 0, 0]
colours = [[255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255]]
colour = 0
sense.set_pixel(x, y, colours[colour])

while True:
    for event in sense.stick.get_events():
        #print(event.direction, event.action)
        sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed' and event.direction == 'up':
            if y > 0:
                sense.set_pixel(x, y, clear)
                y -= 1
                sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed' and event.direction == 'down':
            if y < 7:
                sense.set_pixel(x, y, clear)
                y += 1
                sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed' and event.direction == 'right':
            if x < 7:
                sense.set_pixel(x, y, clear)
                x += 1
                sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed' and event.direction == 'left':
            if x > 0:
                sense.set_pixel(x, y, clear)
                x -= 1
                sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed' and event.direction == 'middle':
            colour += 1
            if colour == len(colours):
                colour = 0
            sense.set_pixel(x, y, colours[colour])

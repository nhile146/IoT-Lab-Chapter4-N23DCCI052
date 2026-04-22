from sense_emu import SenseHat
import time

sense = SenseHat()

# 1. Hien thi chu Hello IoT!
sense.show_message('Hello IoT!', text_colour=[0, 255, 0], scroll_speed=0.08)
time.sleep(1)

# 2. Tu thiet ke bieu tuong (Mat cuoi)
y = [255, 255, 0] # Vang
b = [0, 0, 0]     # Den
r = [255, 0, 0]   # Do

smiley = [
    b, b, y, y, y, y, b, b,
    b, y, b, b, b, b, y, b,
    y, b, r, b, b, r, b, y,
    y, b, b, b, b, b, b, y,
    y, b, r, b, b, r, b, y,
    y, b, b, r, r, b, b, y,
    b, y, b, b, b, b, y, b,
    b, b, y, y, y, y, b, b,
]

sense.set_pixels(smiley)
print('Bieu tuong da hien thi.')
time.sleep(5)
sense.clear()

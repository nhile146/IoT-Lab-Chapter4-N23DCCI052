from sense_emu import SenseHat
import time

sense = SenseHat()
sense.show_message('Hello IoT!', text_colour=[0, 255, 0], scroll_speed=0.08)
time.sleep(1)

w = [255, 255, 255] # Trang
b = [0, 0, 0]       # Den

pattern_N = [
    w, b, b, b, b, b, b, w,
    w, w, b, b, b, b, b, w,
    w, b, w, b, b, b, b, w,
    w, b, b, w, b, b, b, w,
    w, b, b, b, w, b, b, w,
    w, b, b, b, b, w, b, w,
    w, b, b, b, b, b, w, w,
    w, b, b, b, b, b, b, w
]
sense.set_pixels(pattern_N)
time.sleep(5)
sense.clear()

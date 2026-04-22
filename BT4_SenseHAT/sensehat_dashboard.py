from sense_emu import SenseHat
import time

sense = SenseHat()

def map_val(val, in_min, in_max, out_max=8):
    res = int((val - in_min) / (in_max - in_min) * out_max)
    return max(0, min(out_max, res))

def draw_bar(y_start, y_end, cols, color):
    for y in range(y_start, y_end + 1):
        for x in range(8):
            sense.set_pixel(x, y, color if x < cols else [0,0,0])

try:
    while True:
        t = sense.get_temperature()
        h = sense.get_humidity()
        
        t_cols = map_val(t, 15, 40)
        draw_bar(0, 2, t_cols, [255, 0, 0])
        
        h_cols = map_val(h, 20, 90)
        draw_bar(3, 5, h_cols, [0, 0, 255])
        
        # Trang thai 6-7
        sc = [0,255,0]
        if t > 35 and h > 80: sc = [255, 0, 0]
        elif t > 35 or h > 80: sc = [255, 255, 0]
        draw_bar(6, 7, 8, sc)
        
        print(f'T: {t:.1f}C ({t_cols} cols) | H: {h:.1f}% ({h_cols} cols)')
        time.sleep(1)
except KeyboardInterrupt:
    sense.clear()

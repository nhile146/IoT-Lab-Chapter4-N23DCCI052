from sense_emu import SenseHat
import random, time

sense = SenseHat()
sense.clear()
px, py = 3, 3
tx, ty = random.randint(0,7), random.randint(0,7)
score = 0

def draw():
    sense.clear()
    sense.set_pixel(tx, ty, [0, 255, 0])   # Muc tieu
    sense.set_pixel(px, py, [255, 255, 255]) # Nhan vat

draw()
while True:
    for e in sense.stick.get_events():
        if e.action == 'pressed':
            if e.direction == 'up' and py > 0: py -= 1
            elif e.direction == 'down' and py < 7: py += 1
            elif e.direction == 'left' and px > 0: px -= 1
            elif e.direction == 'right' and px < 7: px += 1
            elif e.direction == 'middle': sense.show_message(str(score))
            
            if px == tx and py == ty:
                score += 1
                print(f'Ghi ban! Diem: {score}')
                sense.clear([255, 255, 0]) # Flash vang
                time.sleep(0.3)
                tx, ty = random.randint(0,7), random.randint(0,7)
            draw()
    time.sleep(0.05)

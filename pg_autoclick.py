import time
import pyautogui as pg
import random
import os
import argparse

# failsafe
pg.FAILSAFE = True

# to make a folder for the images to be clicked
image_folder = 'pg_img'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

DIR = './pg_img/'
PICS = [file for file in os.listdir(path=DIR) if file[-4:] == '.png' and file[0] != '.']

parser = argparse.ArgumentParser(description='Put images into the "pg_img" folder. Press ctr+c to cancel.')
parser.add_argument('-x', type=int, default=0, help='offset x, default=0')
parser.add_argument('-y', type=int, default=0, help='offset y, default=0')
parser.add_argument('-c', type=int, default=1, help='iteration counter, default=1')
args = parser.parse_args()

offsetX = args.x
offsetY = args.y
counter = args.c

def main(offsetX=0, offsetY=0, counter=1):
    print(PICS)
    while counter > 0:
        for pic in PICS:
            box = pg.locateOnScreen(DIR + pic, grayscale=False)
            if box is not None:
                dw = box.width // 2
                dh = box.height // 2
                x = pg.center(box).x + random.randint(-dw, dw) + offsetX
                y = pg.center(box).y + random.randint(-dh, dh) + offsetY
                print(x, y)
                pg.click(x, y)
                time.sleep(random.random()/4 + 0.2)
        counter -= 1

if __name__ == '__main__':
    try:
        main(offsetX, offsetY, counter)
        print('END')
    except KeyboardInterrupt:
        print(' ---Cancelled---')

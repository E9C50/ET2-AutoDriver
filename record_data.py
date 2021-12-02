import os
import threading
import time

import cv2
import numpy as np
import pygame
from PIL import ImageGrab

angle = 0
brake = 1
throttle = -1

rect = (0, 50, 1024, 818)
image_path = "./dataset/images/"


def get_control():
    pygame.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("识别到的游戏手柄：" + joystick.get_name())
    while True:
        for event in pygame.event.get():
            global throttle, brake, angle
            if event.type == 1536 and event.axis == 5:
                # 右扳机：按下-0.9 松开-1
                throttle = event.value
            if event.type == 1536 and event.axis == 7:
                # 左扳机：按下0.9 松开1
                brake = event.value
            if event.type == 1536 and event.axis == 1:
                # 左摇杆：left -1; right 1
                angle = event.value
        time.sleep(0.01)


def get_screenshot():
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    log_file = open('./dataset/log.txt', 'w')

    try:
        for _ in range(5000):
            screen = ImageGrab.grab(rect)
            cv_image = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
            image_name = image_path + str(time.time()) + '.jpg'
            cv2.imwrite(image_name, cv_image)

            img_data = image_name + " " + str(angle) + " " + str(throttle) + " " + str(brake)
            log_file.write(img_data + '\n')
            print(str(_) + img_data)

            cv2.imshow('image', cv_image)
            cv2.waitKey(3)
    finally:
        log_file.close()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    Thread1 = threading.Thread(target=get_control)
    Thread2 = threading.Thread(target=get_screenshot)
    Thread1.start()
    Thread2.start()

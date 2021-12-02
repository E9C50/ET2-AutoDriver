import os
import time

import cv2
import numpy as np
from PIL import ImageGrab

rect = (0, 50, 1024, 818)
image_path = "./dataset/images/"

if __name__ == '__main__':
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    for _ in range(100):
        screen = ImageGrab.grab(rect)
        cv_image = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
        image_name = image_path + str(time.time()) + '.jpg'
        cv2.imwrite(image_name, cv_image)
        cv2.imshow('image', cv_image)
        cv2.waitKey(3)

    cv2.destroyAllWindows()

import cv2
import paddle
import numpy as np
from paddle import fluid
from PIL import ImageGrab

rect = (0, 50, 1024, 818)
model_dir = "C:\\Users\\fuxin\\Downloads\\EuroTruckSelfDriver-master\\selfDriverInEuroTruck\\model_infer"

paddle.enable_static()
place = fluid.CPUPlace()
fluidExecutor = fluid.Executor(place)
[ap_program, feed_source, target_var] = fluid.io.load_inference_model(
    dirname=model_dir, executor=fluidExecutor)


def img_process(img):
    img = cv2.resize(img, (120, 120))
    img = np.array(img).astype(np.float32)
    img = img.transpose((2, 0, 1))
    img = img[(2, 1, 0), :, :] / 255.0
    img = np.expand_dims(img, axis=0)
    return img


def get_img():
    while True:
        screen = ImageGrab.grab(rect)
        cv_img = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
        np_img = img_process(cv_img)
        result = fluidExecutor.run(program=ap_program, feed={feed_source[0]: np_img}, fetch_list=target_var)
        angle = result[0][0][0]
        brake = result[0][0][1] / 10
        print(str(angle) + ' - ' + str(brake))
        cv2.imshow('image', cv_img)
        cv2.waitKey(3)


if __name__ == '__main__':
    get_img()

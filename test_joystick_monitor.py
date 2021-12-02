import pygame

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("识别到的游戏手柄：" + joystick.get_name())

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == 1536 and event.axis == 5:
                # 右扳机：按下-0.9 松开-1
                value = event.value
                print("油门：" + str(value))
            if event.type == 1536 and event.axis == 7:
                # 左扳机：按下0.9 松开1
                value = event.value
                print("刹车：" + str(value))
            if event.type == 1536 and event.axis == 1:
                # 左摇杆：left -1; right 1
                value = event.value
                print("方向：" + str(value))

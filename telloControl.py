from djitellopy import Tello
import time

tello = Tello() # 首先创建一个Tello的实例对象
tello.connect() # 连接到Tello无人机
tello.takeoff() # Tello的起飞指令
time.sleep(5)
#tello.move_left(100) # Tello向左平移100厘米
tello.rotate_counter_clockwise(90) # Tello在同一高度逆时针旋转90度
#tello.rotate_clockwise(90) # Tello在同一高度顺时针旋转90度
#tello.move_forward(100) # Tello向前飞行100厘米

tello.land() # Tello的降落指令
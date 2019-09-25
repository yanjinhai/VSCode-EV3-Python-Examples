#!/usr/bin/env python3

from ev3dev.ev3 import *

gyro = GyroSensor(INPUT_1)

gyro.MODE_GYRO_ANG

touchy = TouchSensor(INPUT_2)

if touchy.is_pressed:
    print('Pressed!')
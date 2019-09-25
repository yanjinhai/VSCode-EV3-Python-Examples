#!/usr/bin/env python3

from ev3dev.ev3 import *

# Initialize constants
SPEED = 300

# Initialize drive motors
drive_motor_1 = Motor(OUTPUT_B)
drive_motor_2 = Motor(OUTPUT_C)

color_sensor_1 = ColorSensor(INPUT_2)

drive_motor_1.run_forever(speed_sp = 250)
drive_motor_2.run_forever(speed_sp = 250)

#drive_motor_1.wait_until (color_sensor_1.color == ColorSensor.COLOR_BLACK, timeout = 10000)
#drive_motor_2.wait_until (color_sensor_1.color == ColorSensor.COLOR_BLACK, timeout = 10000)

while color_sensor_1.color != ColorSensor.COLOR_BLACK:
    print('Looking for black...')

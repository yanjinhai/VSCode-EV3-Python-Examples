#!/usr/bin/env python3

from ev3dev.ev3 import *

# Initialize constants
SPEED = 300

# Initialize drive motors
drive_motor_1 = Motor(OUTPUT_B)
drive_motor_2 = Motor(OUTPUT_C)

# Initialize color sensor
color_sensor_1 = ColorSensor(INPUT_2)

# Set color sensor to color mode
color_sensor_1.mode = ColorSensor.MODE_COL_COLOR

# Runs motors at speed of SPEED
drive_motor_1.run_forever(speed_sp = SPEED)
drive_motor_2.run_forever(speed_sp = SPEED)

# Waits for the color sensor to detect black
while color_sensor_1.color != ColorSensor.COLOR_BLACK:
    print('Looking for black...')

# Stops the motors
drive_motor_1.stop
drive_motor_2.stop

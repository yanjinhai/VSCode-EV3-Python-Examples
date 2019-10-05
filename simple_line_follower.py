#!/usr/bin/env python3
'''
FLL ev3dev Python Learning Activity

Analyze the following code and determine it's purpose.

Answer the questions along the way to determine the purpose of individual sections of the code.
'''

from ev3dev.ev3 import *

# What does this section do? _________________________
SPEED_SLOW = -50 # Negative speed because the robot is driving backwards
SPEED_FAST = -200 # Negative speed because the robot is driving backwards
drive_motor_1 = Motor(OUTPUT_B)
drive_motor_2 = Motor(OUTPUT_C)
color_sensor_1 = ColorSensor(INPUT_2)

# What does this section do? _________________________
color_sensor_1.mode = ColorSensor.MODE_COL_COLOR

# What does this section do as a whole? _________________________
while True:
    # What does this section do as a whole? _________________________
    if color_sensor_1.color == ColorSensor.COLOR_BLACK:
        # What does this section do? _________________________
        drive_motor_1.run_forever(speed_sp = SPEED_SLOW)
        drive_motor_2.run_forever(speed_sp = SPEED_FAST)    
    else : 
        # What does this section do? _________________________
        drive_motor_1.run_forever(speed_sp = SPEED_FAST)
        drive_motor_2.run_forever(speed_sp = SPEED_SLOW)    


'''
What does the program as a whole do? ____________________________________
'''
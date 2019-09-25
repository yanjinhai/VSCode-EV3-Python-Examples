#!/usr/bin/env python3
'''More advanced demo on driving robot movement'''

from ev3dev.ev3 import *
import sys

# Initialize drive motors
drive_motor_1 = Motor(OUTPUT_B)
drive_motor_2 = Motor(OUTPUT_C)


# Define drive test function
def drive(pos1, pos2, spd1, spd2):
    '''
    Moves the robot forward, backward, or turns in place.

    pos = number of degrees each motor turns

    spd = absolute speed of both motors
    
    md1 = movement direction of drive_motor_1 (1 or -1)
    
    md2 = movement direction of drive_motor_2 (1 or -1)
    '''
    
    # If something doesn't make sense, exit the program
    if spd1 > 1000 or spd1 < -1000 or spd2 > 1000 or spd2 < -1000:
        print("Error: You can't have a speed above 1000 or below -1000!")
        sys.exit()

    # Run the motors
    # Note: position values can be negative, but not speed values.
    drive_motor_1.run_to_rel_pos(position_sp = pos1, speed_sp = spd1)
    drive_motor_2.run_to_rel_pos(position_sp = pos2, speed_sp = spd2)

    # Wait for current actions to finish
    drive_motor_1.wait_while('running')
    drive_motor_2.wait_while('running')


print('New drive function')

# Move forward by 800 degrees at a speed of 250
drive(800, 800, 250,  250)

# Turn one way by 800 degrees at a speed of 250
drive(800, -800, 250, 250)

# Turn the other way by 800 degrees at a speed of 250
drive(-800, 800, 250, 250)

# Move backwards by 800 degrees at a speed of 250
drive(-800, -800, 250, 250)

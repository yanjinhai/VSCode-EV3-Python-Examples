#!/usr/bin/env python3
'''More advanced demo on driving robot movement'''

from ev3dev.ev3 import *
import sys

#Initialize drive motors
drive_motor_1 = Motor(OUTPUT_B)
drive_motor_2 = Motor(OUTPUT_C)

#Define drive function
def drive(pos, spd, md1, md2):
    '''
    Moves the robot forward, backward, or turns in place.

    pos = number of degrees each motor turns

    spd = absolute speed of both motors
    
    md1 = movement direction of drive_motor_1 (1 or -1)
    
    md2 = movement direction of drive_motor_2 (1 or -1)
    '''
    
    #If something doesn't make sense, exit the program
    if spd > 1000 or spd < -1000:
        print("Error: You can't have a speed above 1000 or below -1000!")
        sys.exit()
    if (md1 != 1 and md1 != -1) or (md2 != 1 and md2 != -1):
        print('Error: The movement direction of a motor should be either 1(forward) or -1(backward).')
        sys.exit()
    

    #Run the motors
    drive_motor_1.run_to_rel_pos(position_sp = pos, speed_sp = spd * md1)
    drive_motor_2.run_to_rel_pos(position_sp = pos, speed_sp = spd * md2)

    #Wait for current actions to finish
    drive_motor_1.wait_while('running')
    drive_motor_2.wait_while('running')


#Move forward by 800 degrees at a speed of 250
drive(800, 250, 1, 1)

#Turn one way by 800 degrees at a speed of 250
drive(800, 250, -1, 1)

#Turn the other way by 800 degrees at a speed of 250
drive(800, 250, 1, -1)

#Move backwards by 800 degrees at a speed of 250
drive(800, 250, -1, -1)

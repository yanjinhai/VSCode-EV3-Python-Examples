#!/usr/bin/env python3

#Import ev3dev's module for ev3 robots.
from ev3dev.ev3 import *

#Initialize drive motors
drive_motor_1 = Motor(OUTPUT_B)
drive_motor_2 = Motor(OUTPUT_C)

#Move forward by a certain amount at a certain speed.
#Run both drive motors at speed 250 in the same direction until their rotational position values increases by 800. 
drive_motor_1.run_to_rel_pos(position_sp = 800, speed_sp = 250)
drive_motor_2.run_to_rel_pos(position_sp = 800, speed_sp = 250)

#Wait for current actions to finish
drive_motor_1.wait_while('running')
drive_motor_2.wait_while('running')

#Move forward by a certain amount at a certain speed.
#Run both drive motors at speed 250 in opposite directions until their rotational position values increases by 800. 
drive_motor_1.run_to_rel_pos(position_sp = 800, speed_sp = -250)
drive_motor_2.run_to_rel_pos(position_sp = 800, speed_sp = 250)

#Wait for current actions to finish
drive_motor_1.wait_while('running')
drive_motor_2.wait_while('running')

#Move forward by a certain amount at a certain speed.
#Run both drive motors at speed 250 in opposite directions until their rotational position values increases by 800. 
drive_motor_1.run_to_rel_pos(position_sp = 800, speed_sp = 250)
drive_motor_2.run_to_rel_pos(position_sp = 800, speed_sp = -250)

#Wait for current actions to finish
drive_motor_1.wait_while('running')
drive_motor_2.wait_while('running')

#Move forward by a certain amount at a certain speed.
#Run both drive motors at speed 250 in the same direction until their rotational position values increases by 800. 
drive_motor_1.run_to_rel_pos(position_sp = 800, speed_sp = -250)
drive_motor_2.run_to_rel_pos(position_sp = 800, speed_sp = -250)

#Wait for current actions to finish
drive_motor_1.wait_while('running')
drive_motor_2.wait_while('running')
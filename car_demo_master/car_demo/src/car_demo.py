#!/usr/bin/env python
import rospy
import time
from prius_msgs.msg import Control


rospy.init_node('car_demo')
pub = rospy.Publisher('prius', Control, queue_size=20)
rate = rospy.Rate(2)
command = Control()
rospy.loginfo('start')
while not rospy.is_shutdown():

	current_key = raw_input('use keyboard strokes to move car')
	
	if(current_key == 'w'):
		command.shift_gears = Control.FORWARD
		command.throttle = 1.0
		command.brake =0.0
		command.steer= 0.0
		pub.publish(command)
	if(current_key == 's'):
		command.shift_gears = Control.REVERSE
		command.throttle = 1.0
		command.brake =0.0
		command.steer= 0.0
		pub.publish(command)
	if(current_key == 'a'):
		command.shift_gears = Control.FORWARD
		command.throttle = 0.5
		command.brake =0.0
		command.steer= 0.8
		pub.publish(command)
	if(current_key == 'd'):
		command.shift_gears = Control.FORWARD
		command.throttle = 0.5
		command.brake =0.0
		command.steer= -0.8
		pub.publish(command)
	if(current_key == 'f'):
		command.shift_gears = Control.NO_COMMAND
		command.throttle = 0.0
		command.brake =1.0
		command.steer= 0.0
		pub.publish(command)

          
	pub.publish(command)     
rospy.spin()

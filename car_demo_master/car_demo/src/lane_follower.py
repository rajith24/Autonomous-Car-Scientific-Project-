#!/usr/bin/env python

import roslib
import sys
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import time
from prius_msgs.msg import Control



class LineFollower(object):
	
	def __init__(self):
		
		self.bridge_object = CvBridge()
		self.image_sub = rospy.Subscriber("/prius/front_camera/image_raw", Image, self.camera_callback)
		self.cmd_vel_pub = rospy.Publisher('prius', Control, queue_size=20)
		self.twist = Control()
	def camera_callback(self,data):
		
		cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding = "bgr8")
		
		height, width, channels = cv_image.shape
		descentre = 80
		rows_to_watch = 20
		
		crop_img = cv_image[(height)/2+descentre:(height)/2+(descentre+rows_to_watch)][1:width]

		
		hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
		
		lower_black = np.array([0,0,0], dtype=np.uint8)
		upper_black = np.array([100,15,100], dtype=np.uint8)


		mask = cv2.inRange(hsv, lower_black, upper_black)

		res = cv2.bitwise_and(crop_img, crop_img, mask = mask)
		
		m = cv2.moments(mask, False)
		
		
		if(m['m00'] > 0):
			cx, cy = m['m10']/m['m00'], m['m01']/m['m00']
		

			cv2.circle(res, (int(cx), int(cy)), 10, (0,0,255), -1)
	
			error_x = cx - width/2
			self.twist.shift_gears = Control.FORWARD
			self.twist.throttle = 1.0
			self.twist.steer = -error_x/100
			self.cmd_vel_pub.publish(self.twist)


		cv2.imshow("Original", cv_image)
		#cv2.imshow("Cropped Image", crop_img)
		#cv2.imshow("Mask", mask)
		cv2.imshow("Res", res)
		
		cv2.waitKey(1)





rospy.init_node("white_follower", anonymous = True)
line_follower_object = LineFollower()
rospy.spin()

	

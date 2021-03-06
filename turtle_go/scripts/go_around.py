#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

BURGER_MAX_LIN_VEL = 0.22
BURGER_MAX_ANG_VEL = 2.84

WAFFLE_MAX_LIN_VEL = 0.26
WAFFLE_MAX_ANG_VEL = 1.82

LIN_VEL_STEP_SIZE = 0.01
ANG_VEL_STEP_SIZE = 0.1

def go_straight():

	rospy.init_node('turtle_go_straight')

	pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

	rate=rospy.Rate(10)

	twist = Twist()

	twist.linear.x = 0.2
	twist.angular.z = 0.05

	while not rospy.is_shutdown():
		pub.publish(twist)
		rate.sleep()


if __name__ == '__main__':
	try:
		go_straight()
	except rospy.ROSInterruptExceptiion:
		pass

		

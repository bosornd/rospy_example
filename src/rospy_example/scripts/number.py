#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

import sys, random

def generate_number(topic):
    rospy.init_node('number', anonymous=True)

    pub = rospy.Publisher(topic, Int32, queue_size=10)

    rate = rospy.Rate(333) # 333hz
    while not rospy.is_shutdown():
        pub.publish(random.randint(-1, 1))
        rate.sleep()

if __name__ == '__main__':
    try:
        generate_number(sys.argv[1])
    except rospy.ROSInterruptException:
        pass

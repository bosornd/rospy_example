#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

class CompareNumbers:
    def __init__(self):
        self.number1 = 0
        self.number2 = 0

        rospy.init_node('compare', anonymous=True)

        rospy.Subscriber('number1', Int32, self.number1_cb)
        rospy.Subscriber('number2', Int32, self.number2_cb)

        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            self.compare()
            rate.sleep()

    def compare(self):
        if self.number1 == self.number2:
            rate = rospy.Rate(1000)
            rate.sleep()

            print(self.number1, "==", self.number2)
            if self.number1 != self.number2:
                print("changed")
        else:
            print(self.number1, "!=", self.number2)
            if self.number1 == self.number2:
                print("changed")

    def number1_cb(self, msg):
        self.number1 = msg.data

    def number2_cb(self, msg):
        self.number2 = msg.data

if __name__ == '__main__':
    try:
        CompareNumbers()
    except rospy.ROSInterruptException:
        pass

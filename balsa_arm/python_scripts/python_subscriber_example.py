#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState


def callback(cmd_msg):
    cmd_msg_servo1 = cmd_msg.position[1]
    cmd_msg_servo2 = cmd_msg.position[2]
    #cmd_msg_servo3 = cmd_msg.position[3]
    rospy.loginfo("I heard %s", cmd_msg.position[1])

def talker():
    #pub = rospy.Publisher('chatter', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    #rate = rospy.Rate(10) # 10hz
    rospy.Subscriber("/joint_states", JointState, callback)
    #while not rospy.is_shutdown():
    #    msg = cmd_msg.position[1] #cmd_msg_servo1
    #    rospy.loginfo(msg)
    #    pub.publish(msg)
    #    rate.sleep()

    rospy.spin()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python


import rospy
from rosserial_arduino import SerialClient
from serial import SerialException
from time import sleep

import sys


flag = 0

class Foo:

    def call_ft(force_torque):

        #make something from data

        force_x = force_torque.force.x
        force_y = force_torque.force.y
        force_z = force_torque.force.z

        torque_x = force_torque.torque.x
        torque_y = force_torque.torque.y
        torque_z = force_torque.torque.z
        
	global flag
	
        if (force_x >= max_fx) or (force_y >= max_fy) or (force_z >= max_fz) or (torque_x >= max_tx) or (torque_y >= max_ty) or (torque_z >= max_tz):
            flag = 1
	else:
	    pass
	
	return flag 


        rospy.loginfo(rospy.get_caller_id() + "I heard force %s", force_torque.force)
        rospy.loginfo(rospy.get_caller_id() + "torque %s", force_torque.torque)



if __name__=="__main__":

    rospy.init_node("serial_node")
    rospy.loginfo("ROS Serial Python Node")

    port_name = rospy.get_param('~port','/dev/ttyUSB0')
    baud = int(rospy.get_param('~baud','57600'))

    # Number of seconds of sync failure after which Arduino is auto-reset.
    # 0 = no timeout, auto-reset disabled
    auto_reset_timeout = int(rospy.get_param('~auto_reset_timeout','0'))

    # for systems where pyserial yields errors in the fcntl.ioctl(self.fd, TIOCMBIS, \
    # TIOCM_DTR_str) line, which causes an IOError, when using simulated port
    fix_pyserial_for_test = rospy.get_param('~fix_pyserial_for_test', False)

    # TODO: do we really want command line params in addition to parameter server params?
    sys.argv = rospy.myargv(argv=sys.argv)
    if len(sys.argv) >= 2 :
        port_name  = sys.argv[1]

    while not rospy.is_shutdown():
        rospy.loginfo("Connecting to %s at %d baud" % (port_name, baud))

        if (flag == 0):
            #do this
            
            try:
                client = SerialClient(port_name, baud, fix_pyserial_for_test=fix_pyserial_for_test, auto_reset_timeout=auto_reset_timeout)
                client.run()
            except KeyboardInterrupt:
                break
            except SerialException:
                sleep(1.0)
                continue
            except OSError:
                sleep(1.0)
                continue
        else:
            print("Too much force/torque.. cannot execute plan")

#!/usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from std_msgs.msg import String


def balsa_arm_move_group_python_interface():
  
  print "============ Starting move_group_python_interface setup"
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('balsa_arm_move_group_python_interface',
                anonymous=True)
  
  robot = moveit_commander.RobotCommander()
  
  scene = moveit_commander.PlanningSceneInterface()
  
  group = moveit_commander.MoveGroupCommander("balsa_wood_arm")
  
  display_trajectory_publisher = rospy.Publisher(
                                    '/move_group/display_planned_path',
                                    moveit_msgs.msg.DisplayTrajectory,
                                    queue_size=20)
  
  
  #Getting basic information
  
  print "============ Waiting for RVIZ..."
  rospy.sleep(10)
  print "============ Starting move_group_python_interface "
  
  print "============ Reference frame: %s" % group.get_planning_frame()
  
  print "============ End effector: %s" % group.get_end_effector_link()
  
  print "============ Robot Groups:"
  print robot.get_group_names()
  
  print "============ Printing robot state"
  print robot.get_current_state()
  print "============"
  
  
  # Planning to a joint_space goal
  
  group_variable_values = group.get_current_joint_values()
  print "============ Joint values: ", group_variable_values
  
  group_variable_values[0] = 0.1
  group.set_joint_value_target(group_variable_values)
  
  plan1 = group.plan()
  
  print "============ Waiting while RVIZ displays plan..."
  rospy.sleep(5)
  
   ## Moving to a pose goal
  group.execute(plan1)
  
  
  ## When finished shut down moveit_commander.
  moveit_commander.roscpp_shutdown()
  
  ## END_MOTION_PLANNING
  
  print "============ STOPPING"

if __name__=='__main__':
  try:
    balsa_arm_move_group_python_interface()
  except rospy.ROSInterruptException:
    pass

Run these to execute python script:

In a new terminal, launch moveit instance
roslaunch balsa_arm_moveit_config demo.launch

In another terminal, change your directory
cd ~/catkin_ws/src/balsa_arm/balsa_arm_planning/scripts

Under that second terminal, make sure pyton file is executable
chmod +x balsa_arm_move_group_python_interface.py

After that, run the python script
rosrun balsa_arm_planning balsa_arm_move_group_python_interface.py

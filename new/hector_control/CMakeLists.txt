cmake_minimum_required(VERSION 2.8.3)
project(hector_control)

find_package(catkin REQUIRED COMPONENTS
  control_toolbox
  controller_interface
  geometry_msgs
  hector_interface
  hector_uav_msgs
  roscpp
  tf
  tf2_geometry_msgs
  visualization_msgs
  )
include_directories(${catkin_INCLUDE_DIRS})

catkin_package(
    LIBRARIES hector_control
    CATKIN_DEPENDS roscpp
    DEPENDS
)

add_library(hector_control
  src/attitude_controller.cpp
  src/velocity_controller.cpp
  src/position_controller.cpp
  )
target_link_libraries(hector_control ${catkin_LIBRARIES})
add_dependencies(hector_control ${catkin_EXPORTED_TARGETS})

install(TARGETS hector_control
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch params
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(FILES
  plugin.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

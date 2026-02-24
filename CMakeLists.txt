cmake_minimum_required(VERSION 3.8)
project(ros2_launch_demo)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 1. Find Dependencies (Added std_msgs here)
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# 2. Build Talker (Linked std_msgs here)
add_executable(talker src/talker.cpp)
ament_target_dependencies(talker rclcpp std_msgs)

# 3. Build Listener (Linked std_msgs here)
add_executable(listener src/listener.cpp)
ament_target_dependencies(listener rclcpp std_msgs)

# 4. Install Executables
install(TARGETS
  talker
  listener
  DESTINATION lib/${PROJECT_NAME}
)

# 5. Install Launch Directory
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
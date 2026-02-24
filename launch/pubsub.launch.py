from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. Launch the Talker Node with the required parameter
        Node(
            package='ros2_launch_demo',
            executable='talker',
            name='talker',
            output='screen',
            parameters=[{'message_prefix': 'ROS2'}]  # Requirement: Set prefix to "ROS2"
        ),
        
        # 2. Launch the Listener Node
        Node(
            package='ros2_launch_demo',
            executable='listener',
            name='listener',
            output='screen'
        )
    ])
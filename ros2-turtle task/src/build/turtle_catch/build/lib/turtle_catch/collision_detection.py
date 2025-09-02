import rclpy
from rclpy.node import Node
from turtlesim.srv import Kill
from turtlesim.msg import Pose
from rclpy.qos import qos_profile_sensor_data
import math

class CollisionDetection(Node):
    def __init__(self):
        super().__init__('collision_detection')
        self.base_pose = None
        self.target_poses = {}
        self.sub_base = self.create_subscription(
            Pose, '/turtle1/pose', self.base_pose_callback, qos_profile_sensor_data)
        self.sub_targets = {}  # Will store subscribers for each spawned turtle
        self.get_logger().info("Collision Detection Node has started.")

    def base_pose_callback(self, msg):
        self.base_pose = msg
        self.check_collision()

    def target_pose_callback(self, turtle_name, msg):
        self.target_poses[turtle_name] = msg
        self.check_collision()

    def check_collision(self):
        if self.base_pose:
            for turtle_name, target_pose in self.target_poses.items():
                distance = math.sqrt(
                    (self.base_pose.x - target_pose.x) ** 2 + (self.base_pose.y - target_pose.y) ** 2)
                if distance < 0.5:  # Threshold for "catching" a turtle
                    self.get_logger().info(f'Turtle {turtle_name} caught!')
                    self.kill_turtle(turtle_name)
                    self.target_poses.pop(turtle_name)
                    self.sub_targets.pop(turtle_name).destroy()

    def kill_turtle(self, turtle_name):
        client = self.create_client(Kill, 'kill')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        request = Kill.Request()
        request.name = turtle_name
        client.call_async(request)

    def spawn_target_subscriber(self, turtle_name):
        sub = self.create_subscription(
            Pose, f'/{turtle_name}/pose', lambda msg: self.target_pose_callback(turtle_name, msg), qos_profile_sensor_data)
        self.sub_targets[turtle_name] = sub

def main(args=None):
    rclpy.init(args=args)
    collision_detection = CollisionDetection()
    rclpy.spin(collision_detection)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

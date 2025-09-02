import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import random

class TurtleSpawner(Node):
    def __init__(self):
        super().__init__('turtle_spawner')
        self.spawn_turtle()

    def spawn_turtle(self):
        client = self.create_client(Spawn, 'spawn')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        request = Spawn.Request()
        request.x = random.uniform(1.0, 10.0)
        request.y = random.uniform(1.0, 10.0)
        request.theta = random.uniform(0.0, 6.28)
        request.name = 'turtle2'
        future = client.call_async(request)
        future.add_done_callback(self.spawn_callback)

    def spawn_callback(self, future):
        response = future.result()
        self.get_logger().info(f'Spawned turtle: {response.name}')

def main(args=None):
    rclpy.init(args=args)
    turtle_spawner = TurtleSpawner()
    rclpy.spin(turtle_spawner)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class UltrasonicPublisher(Node):

    def __init__(self):
        super().__init__('ultrasonic_publisher')
        self.publisher_ = self.create_publisher(Float32, 'ultrasonic_data', 10)
        self.timer_ = self.create_timer(0.1, self.publish_sensor_data)  

    def publish_sensor_data(self):
        
        distance = 10.0  
        msg = Float32()
        msg.data = distance
        self.get_logger().info(f"Publishing ultrasonic data: {msg.data}")
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    ultrasonic_publisher = UltrasonicPublisher()
    rclpy.spin(ultrasonic_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class UltrasonicSubscriber(Node):
    def __init__(self):
        super().__init__('ultrasonic_subscriber')
        self.subscription = self.create_subscription(Float32, 'ultrasonic_data', self.listener_callback, 10)

    def listener_callback(self, msg: Float32):
        if msg.data < 20.0:
            self.get_logger().info('Object detected within 20 cm: {:.2f}'.format(msg.data))
        else:
            self.get_logger().info('No object detected: {:.2f}'.format(msg.data))

def main(args=None):
    rclpy.init(args=args)
    ultrasonic_subscriber = UltrasonicSubscriber()
    rclpy.spin(ultrasonic_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
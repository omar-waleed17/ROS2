import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, termios, tty

class TurtleControl(Node):
    def __init__(self):
        super().__init__('turtle_control')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.get_logger().info("Turtle Control Node has started. Use arrow keys to control the turtle.")
        self.control_loop()

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

    def control_loop(self):
        twist = Twist()
        while True:
            key = self.get_key()
            if key == '\x03':  # Ctrl+C
                break
            elif key == 'w':
                twist.linear.x = 2.0
            elif key == 's':
                twist.linear.x = -2.0
            elif key == 'a':
                twist.angular.z = 2.0
            elif key == 'd':
                twist.angular.z = -2.0
            else:
                twist.linear.x = 0.0
                twist.angular.z = 0.0

            self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    turtle_control = TurtleControl()
    rclpy.spin(turtle_control)
    rclpy.shutdown()

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    main()

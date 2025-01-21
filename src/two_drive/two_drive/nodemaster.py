import rclpy
import rclpy.executors
import rclpy.node
import cv2
import numpy as np

from stopper import Stopper
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from enum import Enum

class State(Enum):
    FollowLine = 1
    TurnOnObject = 2
    Error = 3

class Driver(rclpy.node.Node):
    def __init__(self):
        super().__init__('driver')

        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
                                          history=rclpy.qos.HistoryPolicy.KEEP_LAST,
                                          depth=1)
        self.stateint = 1 # 1 is for Follow 2 is for Turn 3 is Error
        self.line_msg = Twist()
        self.laser_msg = Twist()

        #self.state = State(1)

        self.subscription_laser = self.create_subscription(Twist, 'laser', self.laser_callback, qos_profile=qos_policy)
        self.subscription_line = self.create_subscription(Twist, 'line', self.line_callback, qos_profile=qos_policy)

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 1)

        timer_period = 0.2
        self.my_timer = self.create_timer(timer_period, self.timer_callback )

    def laser_callback(self, msg):

        if(msg.angular.z == 0.0):
            #self.state = State.FollowLine
            self.stateint = 1
        elif(msg.angular.z != 0.0):
            #self.state = State.TurnOnObject
            self.stateint = 2
        else:
            #self.state = State.Error
            self.stateint = 3
        self.laser_msg = msg

    def line_callback(self, msg):

        self.line_msg = msg

    def timer_callback(self):
        #self.get_logger().info("DriverLogic")
        if(self.stateint == 1):
            self.get_logger().info("using LineMsg")
            msg = self.line_msg
        elif(self.stateint == 2):
            self.get_logger().info("using LaserMsg")
            msg = self.laser_msg
        else:
            if not self.node_follow.active:
                self.get_logger().info(f"Activating LineFollow (distance: {self.front_distance})")
                self.node_turn.deactivate()
                self.node_follow.activate()
        #self.front_distance -= 1 
        #print(self.front_distance)

        ''' if(front_dist < turn_dist and front_dist!=0 and self.current_state == 'NODE_Follow'):
            node_follow.destroy_node()
            self.get_logger().info('Switching to NODE_Turn.')
            self.activate_node_turn()
        else: #elif front_dist >= turn_dist and self.current_state == 'NODE_Turn':
            node_turn.destroy_node()
            self.get_logger().info('Switching to NODE_Follow.')
            self.activate_node_follow() '''

def main(args=None):

    print('Hi from NodeMaster')
    rclpy.init(args=args, signal_handler_options=rclpy.SignalHandlerOptions.NO)
    driver_node = Driver()
    
    try:
        rclpy.spin(driver_node)

        rclpy.spin(driver_node)

    except KeyboardInterrupt:
        stop = Stopper()

    finally:
        driver_node.destroy_node()
        stop.destroy_node()
        rclpy.shutdown()
        print('Shutting Down NodeMaster')
        print('Shutting Down NodeMaster')


if __name__ == '__main__':
    main()
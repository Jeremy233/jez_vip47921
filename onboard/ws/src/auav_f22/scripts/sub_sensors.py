#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from px4_msgs.msg import SensorCombined

class SensorCombinedNode(Node):

	def __init__(self):
		super().__init__("sensor_subscriber")
		self.sensor_subscriber = self.create_subscription(
			SensorCombined, "/SensorCombined_PubSubTopic", 
			self.sensor_callback, 10)

	def sensor_callback(self, msg:SensorCombined):
		self.get_logger().info(str(msg))
		

def main(args=None):
	rclpy.init(args=args)
	node = SensorCombinedNode()
	rclpy.spin(node)
	rclpy.shutdown()
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class RGBDImageNode(Node):

	def __init__(self):
		super().__init__("RGBDImage_subscriber")
		self.RGBDImage_subscriber = self.create_subscription(RGBDImage, "/rgbd_camera/depth_image", self.sensor_callback, 10)

	def sensor_callback(self, msg:RGBDImage):
		self.get_logger().info(str(msg))
		

def main(args=None):
	rclpy.init(args=args)
	node = RGBDImageNode()
	rclpy.spin(node)
	rclpy.shutdown()
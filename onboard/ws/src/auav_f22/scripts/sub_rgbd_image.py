#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import time
import os.path

class RGBDImageNode(Node):

	def __init__(self):
		super().__init__("RGBDImage_subscriber")
		self.RGBDImage_subscriber = self.create_subscription(Image, 
		"/rgbd_camera/depth_image", self.sensor_callback, 10)
		self.rgbd_image = None

	def sensor_callback(self, msg:Image):
		self.rgbd_image = msg.data
		i = 0
		while i < 10:
				check_file = "output/rgbd_image" + str(i) + ".txt"
				file_exist = os.path.exists(check_file)
				if file_exist is False:
					file_write = "output/rgbd_image" + str(i) + ".txt"
					f_new = open(file_write, "w+")
					f_new.write(str(self.rgbd_image))
					f_new.close()
					i += 1
				else:
					i += 1
		self.get_logger().info("writing rgbd_image files")



def main(args=None):
	rclpy.init(args=args)
	rgbd_image = RGBDImageNode()
	rclpy.spin(rgbd_image)
	rclpy.shutdown()

if __name__ == '__main__':
	main()
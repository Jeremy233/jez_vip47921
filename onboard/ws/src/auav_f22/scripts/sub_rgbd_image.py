#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import time

class RGBDImageNode(Node):

	def __init__(self):
		super().__init__("RGBDImage_subscriber")
		self.RGBDImage_subscriber = self.create_subscription(RGBDImage, "/rgbd_camera/depth_image", self.sensor_callback, 10)
		self.write_check = True
		self.file_count = 0
		self.rgbd_image = None

	def write_file(self):
		if self.write_check is True:
			file_name = "./output/rgbd_image" + str(self.file_count) + ".txt"
			f = open(file_name, "w")
			for i in self.rgbd_image:
				f.write(str(i) + '\n')
			f.close

	def sensor_callback(self, msg:RGBDImage):
		self.rgbd_image = msg.data
		# write data to txt file, stop when wrote 100 txts
		while self.file_count > 0:
			if self.file_count > 100:
				self.file_count = -1
			else:
				self.write_file()
				time.sleep(0.1)
			self.file_count += 1
			
		self.get_logger().info("rgbd image wrote") # subscribe from the node



def main(args=None):
	rclpy.init(args=args)
	rgbd_image = RGBDImageNode()
	rclpy.spin(rgbd_image)
	rclpy.shutdown()

if __name__ == '__main__':
	main()
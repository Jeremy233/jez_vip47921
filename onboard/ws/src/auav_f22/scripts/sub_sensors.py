#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from px4_msgs.msg import SensorCombined
import time

class SensorCombinedNode(Node):

	def __init__(self):
		super().__init__("sensor_subscriber")
		self.sensor_subscriber = self.create_subscription(SensorCombined, "/SensorCombined_PubSubTopic", self.sensor_callback, 10)
		self.write_check = True
		self.file_count = 0
		self.sensor_data = None

	def write_file(self):
		if self.write_check is True:
			file_name = "./output/sensor_comb" + str(self.file_count) + ".txt"
			f = open(file_name, "w")
			for i in self.sensor_comb:
				f.write(str(i) + '\n')
			f.close

	def sensor_callback(self, msg:SensorCombined):
		self.sensor_comb = msg.data
		# write data to txt file, stop when wrote 100 txts
		while self.file_count > 0:
			if self.file_count > 100:
				self.file_count = -1
			else:
				self.write_file()
				time.sleep(0.1)
			self.file_count += 1

		self.get_logger().info("sensor wrote")

def main(args=None):
	rclpy.init(args=args)
	node = SensorCombinedNode()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == '__main__':
	main()
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from px4_msgs.msg import SensorCombined
import time
import os.path

class SensorCombinedNode(Node):

	def __init__(self):
		super().__init__("sensor_subscriber")
		self.sensor_subscriber = self.create_subscription
		(SensorCombined, "/SensorCombined_PubSubTopic", self.sensor_callback, 10)
		self.sensor_data = None

	def sensor_callback(self, msg:SensorCombined):
		self.sensor_comb = msg
		i = 0
		while i < 10:
				check_file = "output/sensor_data" + str(i) + ".txt"
				file_exist = os.path.exists(check_file)
				if file_exist is False:
					file_write = "output/sensor_data" + str(i) + ".txt"
					f_new = open(file_write, "w+")
					f_new.write(str(self.sensor_comb))
					f_new.close()
					i += 1
				else:
					i += 1
		self.get_logger().info("writing sensor_data files")

def main(args=None):
	rclpy.init(args=args)
	node = SensorCombinedNode()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == '__main__':
	main()
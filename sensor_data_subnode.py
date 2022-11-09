#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from px4_msgs.msg import SensorCombined

class SensorInfoNode(Node):

  def __init__(self):
    super().__init__("sensor_subscriber")
    self.sensor_subscriber = self.create_subscription(SensorCombined, 
    '/SensorCombined_PubSubTopic', self.sensor_callback, 10)
    self.timestamp = 0
    self.gyro_rad = []
    self.gyro_integral = 0
    self.accelerometer_timestamp = 0
    self.accelerometer_m_s2 = []
    self.accelerometer_integral = 0
    self.accelerometer_clipping = 0

  def sensor_callback(self, msg:SensorCombined):
    line = msg.data
    line_data = line.replace("px4_msgs.msg.SensorCombined", "")
    line_data1 = line_data.lstrip("(").rstrip(')')
    line_data2 = line_data1.split(", ")
    self.timestamp = int(line_data2[0].lstrip("timestamp="))
    str_x = float(line_data2[1].lstrip("gyro_rad=array(["))
    self.gyro_rad.append(str_x)
    str_y = float(line_data2[2])
    self.gyro_rad.append(str_y)
    str_z = float(line_data2[3].rstrip("]'"))
    self.gyro_rad.append(str_z)
    self.gyro_integral = int(line_data2[5].lstrip("gyro_integral_dt="))
    self.accelerometer_timestamp = int(line_data2[6].lstrip("accelerometer_timestamp_relative="))
    str_x1 = float(line_data2[7].lstrip("accelerometer_m_s2=array([ "))
    self.accelerometer_m_s2.append(str_x1)
    str_y1 = float(line_data2[8].lstrip(" "))
    self.accelerometer_m_s2.append(str_y1)
    str_z1 = float(line_data2[9].rstrip("]"))
    self.accelerometer_m_s2.append(str_z1)
    self.accelerometer_integral = int(line_data2[11].lstrip("accelerometer_integral_dt="))
    self.accelerometer_clipping = int(line_data2[12].lstrip("accelerometer_clipping="))

def main(args=None):
  rclpy.init(args=args)
  sensor_info_node = SensorInfoNode()
  rclpy.spin(sensor_info_node)
  rclpy.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
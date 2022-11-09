#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# this node is for depth image of rgbd camera
class RGBImageNode(Node): 

  def __init__(self):
    super().__init__("RGB_image_subscriber")
    self.RGB_image_subscriber = self.create_subscription(Image, 
    '/rgbd_camera/image', self.rgb_callback, 10)

  def rgb_callback(self, msg:Image):
    ros2_image = msg.data
    bridge = CvBridge()
    global cv_image
    cv_image = bridge.imgmsg_to_cv2(ros2_image, desired_encoding='bgr8')

    self.get_loggerr().info("cv2 image")

def main(args=None):
  rclpy.init(args=args)
  rgb_image_node = RGBImageNode()
  rclpy.spin(rgb_image_node)
  rclpy.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
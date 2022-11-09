#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# this node is for depth image of rgbd camera
class DepthImageNode(Node): 

  def __init__(self):
    super().__init__("Depth_image_subscriber")
    self.Depth_image_subscriber = self.create_subscription(Image, 
    '/rgbd_camera/depth_image', self.depth_callback, 10)

  def depth_callback(self, msg:Image):
    ros2_image = msg.data
    bridge = CvBridge()
    global cv_image
    # need to find how to get depth channel in cv2
    cv_image = bridge.imgmsg_to_cv2(ros2_image, desired_encoding='bgr8')

    self.get_loggerr().info("cv2 image")

def main(args=None):
  rclpy.init(args=args)
  depth_image_node = DepthImageNode()
  rclpy.spin(depth_image_node)
  rclpy.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
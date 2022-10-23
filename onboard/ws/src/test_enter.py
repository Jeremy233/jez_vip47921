import subprocess

p = subprocess.Popen("ros2 topic list", stdout=subprocess.PIPE, shell=True)
p_return = p.communicate()[0]
p_decode = p_return.decode("utf-8")

topic_list = p_decode.split('\n')
for i in topic_list: 
	if (i == '/rgbd_camera/depth_image'):
		print("found")
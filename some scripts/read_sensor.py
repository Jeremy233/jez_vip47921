class Sensor_data():

	def __init__(self):
		self.timestamp = 0
		self.gyro_rad = []
		self.gyro_integral = 0
		self.accelerometer_timestamp = 0
		self.accelerometer_m_s2 = []
		self.accelerometer_integral = 0
		self.accelerometer_clipping = 0

	def read(self):
		path = "sensor_data0.txt"
		f =open(path, "r")
		line = f.readline()
		f.close()
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

def printSensor(sensor_obj):
	print("timestamp is " + str(sensor_obj.timestamp))
	print(sensor_obj.gyro_rad)
	print("gyro_rad is x=" + str(sensor_obj.gyro_rad[0]) + "y=" + str(sensor_obj.gyro_rad[1]) + "z=" + str(sensor_obj.gyro_rad[2]))
	print("gyro_integral is " + str(sensor_obj.gyro_integral))
	print("accelerometer_timestamp is " + str(sensor_obj.accelerometer_timestamp))
	print("accelerometer_m_s2 is x=" + str(sensor_obj.accelerometer_m_s2[0]) + "y=" + str(sensor_obj.accelerometer_m_s2[1]) + "z=" + str(sensor_obj.accelerometer_m_s2[2]))
	print("accelerometer_integral is " + str(sensor_obj.accelerometer_integral))
	print("accelerometer_clipping is " + str(sensor_obj.accelerometer_clipping))

if __name__ == "__main__":
	sensor_data = Sensor_data()
	sensor_data.read()
	printSensor(sensor_data)

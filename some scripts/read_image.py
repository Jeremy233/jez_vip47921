import numpy as np

def read(filepath):
    f =open(filepath, "r")
    line = f.readline().lstrip("array('B', [").rstrip("])").split(", ")
    f.close()
    print(len(line))
    red_list = []
    green_list = []
    blue_list = []
    depth_list = []

    for i in range(0, len(line), 4):
        red_list.append(line[i])
        green_list.append(line[i + 1])
        blue_list.append(line[i + 2])
        depth_list.append(line[i + 3])




if __name__ == "__main__":
    filepath = "rgbd_image0.txt"
    read(filepath)
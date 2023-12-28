import cv2
import numpy as np
from scipy.spatial import distance
import re
def read_landmarks_from_txtd(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        landmarks = []
        for line in lines:
            if 'shape' in line:
                continue
            landmark_str = line.strip()[1:-1]  # Remove brackets and leading space
            landmark = [int(coord) for coord in landmark_str.split()]
            landmarks.append(landmark)
        return np.array(landmarks)
def read_landmarks_from_txt(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        landmarks = []
        for line in lines:
            if 'shape' in line:
                continue
            # 使用正则表达式提取数字
            landmark_str = re.findall(r'\d+', line)
            landmark = list(map(int, landmark_str))
            landmarks.append(landmark)
        return np.array(landmarks)
def shape_matching(landmarks1, landmarks2):
    # 计算形状描述子（Hu矩）
    moments1 = cv2.moments(landmarks1)
    hu_moments1 = cv2.HuMoments(moments1).flatten()

    moments2 = cv2.moments(landmarks2)
    hu_moments2 = cv2.HuMoments(moments2).flatten()

    # 使用欧氏距离进行形状匹配
    dist = distance.euclidean(hu_moments1, hu_moments2)
    return dist

# 读取特征点
landmarks1 = read_landmarks_from_txt("01.txt")  # 请替换成你的特征点文件路径
landmarks2 = read_landmarks_from_txt("03.txt")  # 请替换成你的特征点文件路径

# 进行形状匹配
matching_distance = shape_matching(landmarks1, landmarks2)

# 输出匹配距离
print("Shape Matching Distance:", matching_distance)

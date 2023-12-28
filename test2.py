import cv2
import numpy as np

def load_keypoints(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    keypoints = np.array([[float(coord) for coord in line.split()] for line in lines])
    return keypoints

def calculate_hu_moments(keypoints):
    # 从特征点中提取轮廓
    contours = np.array(keypoints, dtype=np.int32)
    # 构建二值图像
    img = np.zeros((500, 500), dtype=np.uint8)
    cv2.drawContours(img, [contours], 0, 255, thickness=cv2.FILLED)
    # 计算Hu矩
    moments = cv2.moments(img)
    hu_moments = cv2.HuMoments(moments).flatten()
    return hu_moments

def calculate_similarity(hu_moments1, hu_moments2):
    # 计算Hu矩之间的相似性
    similarity = cv2.matchShapes(hu_moments1, hu_moments2, cv2.CONTOURS_MATCH_I1, 0.0)
    return similarity

# 两组特征点文件的路径
file_path1 = '111.txt'
file_path2 = '222.txt'

# 加载特征点
keypoints1 = load_keypoints(file_path1)
keypoints2 = load_keypoints(file_path2)

# 计算Hu矩
hu_moments1 = calculate_hu_moments(keypoints1)
hu_moments2 = calculate_hu_moments(keypoints2)

# 计算相似性
similarity = calculate_similarity(hu_moments1, hu_moments2)

# 打印相似性
print(f"Similarity between the two sets of keypoints: {similarity}")
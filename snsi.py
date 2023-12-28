import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# 读取特征点
landmarks1 = np.array([[191,595],[362,964],
 [423, 955],
 [457, 924],
 [469, 885],
 [469, 840],
 [460, 798],
 [460, 746],
 [472, 698],
 [482, 652],
 [492, 606],
 [205, 641],
 [283, 865],
 [317, 935],
 [440, 871],
 [409, 929],
 [186, 505],
 [212, 539],
 [192, 531],
 [505, 509],
 [491, 533],
 [503, 527],
 [214, 695],
 [223, 741],
 [230, 796],
 [221, 848],
 [228, 898],
 [254, 936],
 [301, 960]])  # 请替换成你的特征点数组
landmarks2 = np.array([[180, 600],
 [348, 965],
 [413, 956],
 [443, 923],
 [458, 884],
 [464, 841],
 [454, 785],
 [461, 740],
 [473, 694],
 [478, 648],
 [488, 601],
 [191, 650],
 [266, 881],
 [301, 937],
 [424, 881],
 [386, 943],
 [182, 502],
 [210, 540],
 [187, 531],
 [497, 503],
 [477, 535],
 [496, 527],
 [202, 701],
 [217, 749],
 [224, 799],
 [223, 851],
 [233, 907],
 [255, 942],
 [292, 961]])  # 请替换成你的特征点数组

# 显示图像和特征点
def plot_image_with_landmarks(image, landmarks):
    plt.imshow(image)
    plt.scatter(landmarks[:, 0], landmarks[:, 1], c='red', marker='o')
    plt.show()

# 读取图像
image1 = plt.imread("03_0002_FRONT_1.jpg")  # 请替换成你的图像文件路径
image2 = plt.imread("03_0002_FRONT_2.jpg")  # 请替换成你的图像文件路径

# 显示图像和特征点
plot_image_with_landmarks(image1, landmarks1)
plot_image_with_landmarks(image2, landmarks2)

# 三角剖分
tri1 = Delaunay(landmarks1)
tri2 = Delaunay(landmarks2)

# 在图像上绘制三角形
plt.triplot(landmarks1[:, 0], landmarks1[:, 1], tri1.simplices, color='blue')
plt.triplot(landmarks2[:, 0], landmarks2[:, 1], tri2.simplices, color='green')
plt.show()

import cv2

# 读取图像
image = cv2.imread("03_0002_FRONT_1.jpg")

# 将图像转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 创建ORB对象
orb = cv2.ORB_create()

# 检测关键点和计算描述符
keypoints, descriptors = orb.detectAndCompute(gray, None)

# 在图像上绘制关键点
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)

# 显示图像
cv2.imshow("Image with ORB Keypoints", image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()

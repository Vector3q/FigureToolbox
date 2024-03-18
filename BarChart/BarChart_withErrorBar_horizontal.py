import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'

plt.figure(figsize=(13, 6))
# 构造y轴刻度标签、数据
labels = ['G1', 'G2', 'G3', 'G4', 'G5']

first = [0, 0, 0, 0, 0]

# 2/24
# second = [4, 3.7, 4.3, 3.3, 3.7]
# third = [2.7,3.7,2.7, 4, 3.3]
# second = [4, 4.3, 4.7, 4, 4.3]
# third = [4, 2.3, 1.7,2,2.3]

# Before 
second = [3.18, 4.09, 4, 3.73, 3.64]
# [3.9, 4.3, 4.4, 3.8, 3.8]
# [4, 4.1, 4.3, 4.2, 3.7]
# [3.45, 3.64, 4.09, 3.91, 3.36]
# [3.18, 4.09, 4, 3.73, 3.64]
third = [3, 2.55, 2.27, 2.73, 2.73]
# [3.4, 3.5, 3.3, 4.1, 4]
# [3.4, 3.2, 2.1, 2.7, 2.5]
# [2.27, 3.45, 2.09, 3.82, 3.36]
# [3, 2.55, 2.27, 2.73, 2.73]
# second = [2.5, 3.6, 3.9, 2.5, 3.3]
# third = [3.7, 2.7, 2.0,2.7, 2.2]

Question = ["我会愿意经常使用该模式进行拍照","我认为使用该模式进行拍照很简单",
            "我认为该模式中的提示的内容有帮助","我认为我不需要技术人员的支持就能使用该模式进行拍照",
            "我认为该模式进行拍照的过程很连贯","我认为该模式进行拍照的效率高",
            "我满意该模式拍照的结果","我认为该模式对学习摄影构图有帮助",
            "我认为该模式的不同功能被较好整合在一起","我对于使用GB模式进行拍照感到很自信"]

errs_lower = [4, 4, 0, 0, 26, 7, 0, 0]
errs_upper = [62, 6, 0, 0, 33, 6, 0, 0]

# 固定误差线的长度为0.5
error_224 = 0

error_GM = [1.08, 0.83, 0.632, 0.647, 0.81]
# [1.14, 0.78,0.49, 1.08, 0.98]
# [0.894, 0.7, 0.46, 0.6, 0.78]
# [1.03, 1.02, 0.8, 0.7, 0.924]
# [1.08, 0.83, 0.632, 0.647, 0.81]
error_FM = [0.7746, 1.036, 0.9045, 1.104, 0.786]
# [1.2, 1.28, 0.9, 0.94, 1]
# [1.35, 0.87, 1.04, 1.42, 1.02]
# [0.9, 1.03, 0.7, 0.874, 0.924]
# [0.7746, 1.036, 0.9045, 1.104, 0.786]

# 三组数据
plt.subplot(111)
y = np.arange(len(labels))  # y轴刻度标签位置
height = 0.25  # 柱子的高度

# 计算每个柱子在y轴上的位置，保证y轴刻度标签居中
# y - height/2，y + height/2即每组数据在y轴上的位置
bars1 = plt.barh(y - height, first, height, capsize=5)
# 224
# bars2 = plt.barh(y, second, height, label='GB',  color='#8ECFC9', capsize=5)
# bars3 = plt.barh(y + height, third, height, label='FB', color='#FA7F6F', capsize=5)
 #8ECFC9 #FA7F6F
 #82B0D2 #FFBE7A
bars2 = plt.barh(y, second, height, xerr=error_GM, label='GM',  color='#82B0D2', capsize=5)
bars3 = plt.barh(y + height, third, height, xerr=error_FM,  label='FM', color='#FFBE7A', capsize=5)
plt.xlabel('Scores')
# y轴刻度标签位置不进行计算
plt.yticks([])

# 添加文字标签说明问题的比较
for i, (bar1, bar2, bar3) in enumerate(zip(bars1, bars2, bars3)):
    plt.text(0, bar1.get_y() + bar1.get_height() / 2,
             Question[i+5], ha='left', va='center', color='black')

plt.gca().invert_yaxis()
plt.legend()

# 设置x轴范围为0到5
plt.xlim(0, 5)

plt.show()








# 三组数据
# plt.subplot(132)
# x = np.arange(len(labels))  # x轴刻度标签位置
# width = 0.25  # 柱子的宽度
# # 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
# # x - width，x， x + width即每组数据在x轴上的位置
# plt.bar(x - width, first, width, label='1')
# plt.bar(x, second, width, label='2')
# plt.bar(x + width, third, width, label='3')
# plt.ylabel('Scores')
# plt.title('3 datasets')
# # x轴刻度标签位置不进行计算
# plt.xticks(x, labels=labels)
# plt.legend()
# # 四组数据
# plt.subplot(133)
# x = np.arange(len(labels))  # x轴刻度标签位置
# width = 0.2  # 柱子的宽度
# # 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
# plt.bar(x - 1.5*width, first, width, label='1')
# plt.bar(x - 0.5*width, second, width, label='2')
# plt.bar(x + 0.5*width, third, width, label='3')
# plt.bar(x + 1.5*width, fourth, width, label='4')
# plt.ylabel('Scores')
# plt.title('4 datasets')
# # x轴刻度标签位置不进行计算
# plt.xticks(x, labels=labels)
# plt.legend()
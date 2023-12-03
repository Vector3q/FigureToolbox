import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(13, 6))
# 构造y轴刻度标签、数据
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
second = [4, 4.1, 3, 3.5, 4.2]
first = [0, 0, 0, 0, 0]
third = [2,2.1,1.0,2.1,3]

# 固定误差线的长度为0.5
error_length = 0.1

# 三组数据
plt.subplot(111)
y = np.arange(len(labels))  # y轴刻度标签位置
height = 0.25  # 柱子的高度

# 计算每个柱子在y轴上的位置，保证y轴刻度标签居中
# y - height/2，y + height/2即每组数据在y轴上的位置
bars1 = plt.barh(y - height, first, height, capsize=5)
bars2 = plt.barh(y, second, height, xerr=error_length, label='GB',  color='#8ECFC9', capsize=5)
bars3 = plt.barh(y + height, third, height, xerr=error_length,  label='FB', color='#FA7F6F', capsize=5)
plt.xlabel('Scores')
# y轴刻度标签位置不进行计算
plt.yticks([])

# 添加文字标签说明问题的比较
for i, (bar1, bar2, bar3) in enumerate(zip(bars1, bars2, bars3)):
    plt.text(0, bar1.get_y() + bar1.get_height() / 2,
             f' Question {i + 1}', ha='left', va='center', color='black')

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
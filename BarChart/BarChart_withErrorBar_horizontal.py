import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'

plt.figure(figsize=(13, 10))
# 构造y轴刻度标签、数据
labels = ['G1', 'G2', 'G3', 'G4', 'G5','G1', 'G2', 'G3', 'G4', 'G5']

first = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 2/24
# second = [4, 3.7, 4.3, 3.3, 3.7]
# third = [2.7,3.7,2.7, 4, 3.3]
# second = [4, 4.3, 4.7, 4, 4.3]
# third = [4, 2.3, 1.7,2,2.3]

# Before 
second = [3.45, 3.64, 4.09, 3.91, 3.36, 3.18, 4.09, 4, 3.73, 3.64]

# [3.45, 3.64, 4.09, 3.91, 3.36]
# [3.18, 4.09, 4, 3.73, 3.64]
third = [2.27, 3.45, 2.09, 3.82, 3.36, 3, 2.55, 2.27, 2.73, 2.73]

# [2.27, 3.45, 2.09, 3.82, 3.36]
# [3, 2.55, 2.27, 2.73, 2.73]
# second = [2.5, 3.6, 3.9, 2.5, 3.3]
# third = [3.7, 2.7, 2.0,2.7, 2.2]
forth = [3.9, 4.3, 4.4, 3.8, 3.8, 4, 4.1, 4.3, 4.2, 3.7]
# [3.9, 4.3, 4.4, 3.8, 3.8]
# [4, 4.1, 4.3, 4.2, 3.7]
fifth = [3.4, 3.5, 3.3, 4.1, 4, 3.4, 3.2, 2.1, 2.7, 2.5]
# [3.4, 3.5, 3.3, 4.1, 4]
# [3.4, 3.2, 2.1, 2.7, 2.5]


Question = ["I think that I would like to use this system frequently", "I think the system is not complex",
            "I think the system was easy to use", "I think that I would not need the support of a technical person to be able to use this system",
            "I found the various functions in this system were well integrated", "I think the system is very efficient",
            "I am very satisfied with the system", "I would image that most people would learn to use this system very quickly",
            "I think this system is consistent", "I feel very confident when using the system"]

errs_lower = [4, 4, 0, 0, 26, 7, 0, 0]
errs_upper = [62, 6, 0, 0, 33, 6, 0, 0]

# 固定误差线的长度为0.5
error_224 = 0

error_GB = [1.213559752 /2, 1.026910636/2, 1.044465936/2, 0.70064905/2, 0.924416278/2, 1.07871978 / 2, 0.831209415/2, 0.632455532/2, 0.646669791/2, 0.809039835/2]
# [1.213559752 /2, 1.026910636/2, 1.044465936/2, 0.70064905/2, 0.924416278/2]
# [1.07871978 / 2, 0.831209415/2, 0.632455532/2, 0.646669791/2, 0.809039835/2]
error_FB = [0.904534034/2, 1.035725481/2, 0.70064905/2, 0.873862898/2, 0.924416278/2, 0.774596669/2, 1.035725481/2, 0.904534034/2, 1.103712743/2, 0.786245393/2]
# [0.904534034/2, 1.035725481/2, 0.70064905/2, 0.873862898/2, 0.924416278/2]
# [0.774596669/2, 1.035725481/2, 0.904534034/2, 1.103712743/2, 0.786245393/2]
error_GM = [1.14/2, 1.02/2, 0.49/2, 1.08/2, 0.98/2, 0.894/2, 0.7/2, 0.46/2, 0.6/2, 0.78/2]
# [1.14/2, 1.02/2, 0.49/2, 1.08/2, 0.98/2]
# [0.894/2, 0.7/2, 0.46/2, 0.6/2, 0.78/2]
error_FM = [1.2/2, 1.28/2, 0.9/2, 0.94/2, 1/2, 1.35/2, 0.87/2, 1.04/2, 1.42/2, 1.02/2]
# [1.2/2, 1.28/2, 0.9/2, 0.94/2, 1/2]
# [1.35/2, 0.87/2, 1.04/2, 1.42/2, 1.02/2]
# 三组数据
plt.subplot(111)
y = np.arange(len(labels))  # y轴刻度标签位置
height = 0.25  # 柱子的高度

base = 0.75
# 计算每个柱子在y轴上的位置，保证y轴刻度标签居中
# y - height/2，y + height/2即每组数据在y轴上的位置
bars1 = plt.barh(y - base * height, first, base * height, capsize=5)
# 224
# bars2 = plt.barh(y, second, height, label='GB',  color='#8ECFC9', capsize=5)
# bars3 = plt.barh(y + height, third, height, label='FB', color='#FA7F6F', capsize=5)
 #8ECFC9 #FA7F6F
 #82B0D2 #FFBE7A
bars2 = plt.barh(y, second, base * height, xerr=error_GB, label='GB',  color='#8ECFC9', capsize=3)
bars3 = plt.barh(y +  base * height, third, base * height, xerr=error_FB,  label='FB', color='#FA7F6F', capsize=3)
bars4 = plt.barh(y + 2 * base * height, forth, base * height, xerr=error_GM, label='GM',  color='#82B0D2', capsize=3)
bars5 = plt.barh(y + 3 * base * height, fifth, base * height, xerr=error_FM,  label='FM', color='#FFBE7A', capsize=3)

plt.xticks(fontsize=18)
plt.xlabel('Score', fontsize=20)
# y轴刻度标签位置不进行计算
plt.yticks([])

# 添加文字标签说明问题的比较
for i, (bar1, bar2, bar3, bar4, bar5) in enumerate(zip(bars1, bars2, bars3, bars4, bars5)):
    plt.text(0 , bar1.get_y() + bar1.get_height() / 2,
             Question[i], ha='left', va='center', color='black',fontsize=10)

plt.gca().invert_yaxis()
plt.legend(fontsize=15)

# 设置x轴范围为0到5
plt.xlim(0, 5.5)

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
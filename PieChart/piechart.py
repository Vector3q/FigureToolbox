import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体  
rcParams['axes.unicode_minus'] = False  # 正确显示负号 
label_now = ['非常熟悉','熟悉']
count_now = [8,4]
color_now = ["#8ECFC9", "#FFBE7A"]
plt.figure(figsize=(6, 3), dpi=300)

# 通过pie
plt.pie(count_now, labels=label_now, autopct='%1.2f%%', colors=color_now)

# 指定显示的pie是正圆
plt.axis('equal')

plt.legend(loc='best')

plt.title("")

plt.savefig('E:\Project\Gits\FigureToolbox\FigureToolbox\PieChart\sample.png',  bbox_inches='tight')
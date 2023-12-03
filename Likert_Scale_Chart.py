import matplotlib.pyplot as plt

# 数据
categories = ['Usability']
gb_scores = [77.79]  # 替换为实际的 GB 模式得分
fb_scores = [77.79]  # 替换为实际的 FB 模式得分

# 创建图表
fig, ax = plt.subplots()

# 绘制柱状图
bar_width = 0.35
index = range(len(categories))
bar_gb = ax.bar(index, gb_scores, bar_width, label='GB Mode')
bar_fb = ax.bar([i + bar_width for i in index], fb_scores, bar_width, label='FB Mode')

# 添加数值标签
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, color='black')

add_labels(bar_gb)
add_labels(bar_fb)

# 设置图表属性
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold', color='black')
ax.set_ylabel('SUS Score', fontsize=12, fontweight='bold', color='black')
ax.set_title('Usability Comparison Between GB and FB Modes', fontsize=14, fontweight='bold', color='black')
ax.legend()

# 显示图表
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# x, err, label, title, color, width
x = [30, 50, 20, 90]
y = [0, 20, 40, 60, 80, 100]
errs = [4, 2, 5, 1]
x_label = ["GM", "GB", "FM", "FB"]
# y_label = ["Not Satisfied", "Slightly Satisfied", "Neutral", "Satisfied", "Extremely Satisfied"]
title_str = 'Averaged Rating of Four Photography Models'
colors = ['#82B0D2', '#8ECFC9', '#FFBE7A', '#FA7F6F'] 
width_x = 0.4


x_np = np.array(x)
y_np = np.array(y)
errs_np = np.array(errs)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
bars = ax.bar(x_label, x_np, yerr=errs_np, capsize=5, color=colors, width=width_x)



ax.set_xticklabels(x_label, fontdict={'fontsize': 12, 'fontweight': 'bold', 'color': 'black'})
ax.set_ylabel('Time (s)', fontdict={'fontsize': 12, 'fontweight': 'bold', 'color': 'black'})
plt.ylim(0, 100)  # 设置y轴刻度范围
ax.set_yticklabels(y_np, fontdict={'fontsize': 12, 'fontweight': 'bold', 'color': 'black'})

plt.subplots_adjust(top=0.85)
plt.show()


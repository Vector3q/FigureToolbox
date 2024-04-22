import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 8),dpi=250)
# x, err, label, title, color, width
# x = [67.725, 45.675, 76.25, 55.50]
x = [3.612, 3.03125, 3.40625, 3.25]
y = [0, 1, 2, 3, 4, 5]
nowerrs = [0,0,0,0]
nowerrs = [0.798/2, 0.876/2, 1.014/2, 0.798/2]
x_label = [" ", "  ", "   ", "    "]
_label = ["GB", "FB", "GM", "FM"]
# y_label = ["Not Satisfied", "Slightly Satisfied", "Neutral", "Satisfied", "Extremely Satisfied"]
title_str = 'Averaged Rating of Four Photography Models'
colors = ['#8ECFC9', '#FA7F6F', '#82B0D2', '#FFBE7A'] 
width_x = 0.4

x_np = np.array(x)
y_np = np.array(y)
errs_np = np.array(nowerrs)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
bars = ax.bar(x_label, x_np,yerr=errs_np, capsize=5, color=colors,  width=width_x)


ax.legend(handles=[bars[0], bars[1], bars[2], bars[3],],
          labels=_label, loc='upper center', bbox_to_anchor=(0.5, 1), ncol=len(_label),fontsize=12)
ax.set_ylabel('Score', fontdict={'fontsize': 18, 'fontweight': 'bold', 'color': 'black'})

plt.ylim(0, 6)  # 设置y轴刻度范围
ax.set_yticklabels(y_np, fontdict={'fontsize': 12, 'fontweight': 'bold', 'color': 'black'})
# ax.legend()
plt.subplots_adjust(top=0.85)
plt.show()


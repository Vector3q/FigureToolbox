import matplotlib.pyplot as plt
import numpy as np

# Original data
y_score = [227.77, 28.91, 183.69, 23.24, 154.21, 24.79, 111.55, 27.75]
y = [0, 100, 200, 300, 400, 500]
errs_lower = [17.9, 8, 30.5, 6.715, 13.3, 6, 10.5, 8.4]
errs_upper = [17.9, 8, 30.5, 6.715, 13.3, 6, 10.5, 8.4]


# x_label = ["GM", "GB", "FM", "FB", "GM", "GB", "FM", "FB"]
x_label = ["", "", "", "", "", "", "", ""]
title_str = 'Averaged Rating of Four Photography Models'
colors = ['#82B0D2', '#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#8ECFC9', '#FFBE7A', '#FA7F6F'] 
width_x = 0.5 

# Grouping data
group1_indices = [0, 1, 2, 3]
group2_indices = [4, 5, 6, 7]
x_group1 = np.arange(len(group1_indices))
x_group2 = np.arange(len(group2_indices)) + len(group1_indices) + 0.8  # Increase the distance between groups

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

errs_1 = [[errs_lower[0], errs_lower[1], errs_lower[2], errs_lower[3]], [errs_upper[0], errs_upper[1], errs_upper[2], errs_upper[3]]]
errs_2 = [[errs_lower[4], errs_lower[5], errs_lower[6], errs_lower[7]], [errs_upper[4], errs_upper[5], errs_upper[6], errs_upper[7]]]

# Plotting bars for each group
# bars_group1 = ax.bar(x_group1, [y_score[i] for i in group1_indices], capsize=4, color=[colors[i] for i in group1_indices], width=width_x, label='Group 1')
# bars_group2 = ax.bar(x_group2, [y_score[i] for i in group2_indices], capsize=4, color=[colors[i] for i in group2_indices], width=width_x)

bars_group1 = ax.bar(x_group1, [y_score[i] for i in group1_indices], yerr=errs_1, capsize=4, color=[colors[i] for i in group1_indices], width=width_x, label='Group 1')
bars_group2 = ax.bar(x_group2, [y_score[i] for i in group2_indices], yerr=errs_2, capsize=4, color=[colors[i] for i in group2_indices], width=width_x)

# Set x-axis ticks and labels
ax.set_xticks(np.concatenate([x_group1, x_group2]))
ax.set_xticklabels([x_label[i] for i in group1_indices + group2_indices], fontdict={'fontsize': 12, 'fontweight': 'bold', 'color': 'black'})

# Set y-axis label and ticks
ax.set_ylabel('Time (s)', fontdict={'fontsize': 12, 'fontweight': 'bold', 'color': 'black'})
plt.ylim(0, 120)
ax.set_yticks(y)
ax.set_yticklabels([str(val) for val in y], fontdict={'fontsize': 12, 'fontweight': 'bold', 'color': 'black'})

# Set legend
legend_labels = ['GM', 'GB', 'FM', 'FB']

ax.legend(handles=[bars_group1[0], bars_group1[1], bars_group1[2], bars_group1[3],
                   bars_group2[0], bars_group2[1], bars_group2[2], bars_group2[3]],
          labels=legend_labels, loc='upper center', bbox_to_anchor=(0.5, 1), ncol=len(legend_labels))

ax.text(0.235, -0.05, 'Group 1', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color='black', fontsize=12, fontweight='bold')
ax.text(0.765, -0.05, 'Group 2', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color='black', fontsize=12, fontweight='bold')
# Set title
# plt.title(title_str, fontsize=14, fontweight='bold')

plt.show()

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(50, 50), dpi=250)
# Original data
y_score = [227.77, 183.69, 28.91,  23.24, 154.21, 111.55, 24.79,  27.75]
y = [0, 80, 160, 240, 320]
errs_lower = [17.9, 30.5, 8,  6.715, 13.3, 10.5, 6,  8.4]
errs_upper = [17.9, 30.5, 8,  6.715, 13.3, 10.5, 6,  8.4]


# x_label = ["GM", "GB", "FM", "FB", "GM", "GB", "FM", "FB"]
x_label = ["", "", "", "", "", "", "", ""]
title_str = 'Averaged Rating of Four Photography Models'
colors = ['#8ECFC9', '#FA7F6F', '#82B0D2', '#FFBE7A', '#8ECFC9', '#FA7F6F', '#82B0D2', '#FFBE7A'] 
width_x = 0.25

# Grouping data
group1_indices = [0, 1, 2, 3]
group2_indices = [4, 5, 6, 7]
x_group1 = np.arange(len(group1_indices))/4
x_group2 = (np.arange(len(group2_indices)) + 5)/4  # Increase the distance between groups

fig = plt.figure(figsize=(8, 6),dpi=250)
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
ax.set_xticklabels([x_label[i] for i in group1_indices + group2_indices], fontdict={'fontsize': 12, 'color': 'black'})

ax.set_ylabel('Time', fontdict={'fontsize': 15, 'color': 'black'})
plt.ylim(0, 380)
ax.set_yticks(y)
ax.set_yticklabels([str(val) for val in y], fontdict={'fontsize': 12, 'color': 'black'})

# Set legend
legend_labels = ['GB', 'FB', 'GM', 'FM']

ax.legend(handles=[bars_group1[0], bars_group1[1], bars_group1[2], bars_group1[3],
                   bars_group2[0], bars_group2[1], bars_group2[2], bars_group2[3]],
          labels=legend_labels, loc='upper center', bbox_to_anchor=(0.5, 1), ncol=len(legend_labels), fontsize=16)

ax.text(0.235, -0.05, 'Group 1', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color='black', fontsize=12)
ax.text(0.765, -0.05, 'Group 2', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color='black', fontsize=12)
# Set title
# plt.title(title_str, fontsize=14, fontweight='bold')

plt.savefig('E:\Project\Gits\FigureToolbox\FigureToolbox\BarChart\SUS.jpg', bbox_inches='tight')
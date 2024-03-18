import matplotlib.pyplot as plt
from datetime import datetime
import json
from itertools import cycle


with open('time_list.json', 'r', encoding='utf-8') as file:
            data = json.load(file)


# 提取第一个数据的时间，以便后续将其他时间减去该时间
first_time = data[0]['time']

# 初始化字典以存储不同视频编号的时间和视频时间
video_data = {}

# 转换时间并提取视频时间
for entry in data:
    video_id = entry['video']
    # 如果视频编号不存在于字典中，则创建一个新的键值对
    if video_id not in video_data:
        video_data[video_id] = {'converted_times': [], 'video_times': []}
    # 将时间转换为秒，并减去第一个数据的时间
    converted_time = (entry['time'] - first_time) / 1000
    video_data[video_id]['converted_times'].append(converted_time)
    video_data[video_id]['video_times'].append(entry['video_time'])

# 绘制图表
for video_id, data in video_data.items():
    plt.plot(data['converted_times'], data['video_times'], marker='o', label=video_id)

plt.xlabel('Time (seconds)')
plt.ylabel('Video Time (seconds)')
plt.title('Video Time vs. Time')
plt.legend()
plt.show()
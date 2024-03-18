import json

# 读取输入文件
input_file = "E:\\Project\\Gits\\FigureToolbox\\FigureToolbox\\Video\\Data\\time_list_baseline.json"
with open(input_file, "r") as infile:
    data = json.load(infile)

# 添加id属性
for i in range(len(data)):
    data[i]["id"] = i + 1

# 写入到新的JSON文件
output_file = "E:\\Project\\Gits\\FigureToolbox\\FigureToolbox\\Video\\Output\\modified_time_list_baseline.json"
with open(output_file, "w") as outfile:
    json.dump(data, outfile, indent=4)
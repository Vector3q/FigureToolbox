import json

# 假设您已经有了包含 JSON 数据的文件，此处命名为data.json
# 如果数据在变量中，可以直接将其传递给 json.loads() 方法
with open('E:\Project\Gits\FigureToolbox\FigureToolbox\Video\info.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 计数器
count = 0

# 遍历数据中的每个条目
for key, value in data['info'].items():
    for item in value['info']:
        # 检查条目是否具有 "repeat_status": 1 并且 "description" 不为空
        if item.get('repeat_status') == 1 and item.get('description'):
            count += 1

print("'description'不为空，'repeat_status': 1的数据条目数：", count)

count = 0

# 遍历数据中的每个条目
for key, value in data['info'].items():
    for item in value['info']:
        # 检查条目是否具有 "repeat_status": 1 并且 "description" 不为空
        if item.get('repeat_status') == 1 and item.get('description') and item.get('humanAdd') == 1:
            count += 1

print("'repeat_status': 1 并且 humanAdd': 1'的数据条目数：", count)

count_different_description = 0

for key, value in data['info'].items():
    for item in value['info']:
        # 检查条目是否具有 "repeat_status": 1
        if item.get('repeat_status') == 1 and item.get('description'):
            # 获取当前条目的 "description" 和 "default" 中的 "description"
            description = item.get('description')
            default_description = item.get('default', {}).get('description')

            # 检查 "description" 和 "default" 中的 "description" 是否相同
            if description != default_description:
                count_different_description += 1

print("'repeat_status': 1中，'description'和'default' 中不同的数量：", count_different_description)

unique_tag_count = {}

# 遍历数据中的每个条目
for key, value in data['info'].items():
    for item in value['info']:
        # 检查条目是否具有 "repeat_status": 1
        if item.get('repeat_status') == 1:
            # 获取当前条目的唯一标签列表
            unique_tags = item.get('unique_tag', [])
            # 对于每个唯一标签，增加对应的计数器
            for tag in unique_tags:
                unique_tag_count[tag] = unique_tag_count.get(tag, 0) + 1

# 输出在 "repeat_status": 1 的条目中，每个唯一标签对应的数据条目数
for tag, count in unique_tag_count.items():
    print(f"在 'repeat_status': 1 的条目中，唯一标签 {tag} 包含 {count} 条数据.")
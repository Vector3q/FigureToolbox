import json

# 读取JSON文件
with open('DataPreProcessing\processedData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 1
# 访问数据
for person in data:
    for key, value in person.items():
        print("User", count)
        count = count + 1
        print("Name:", value['name'])
        print("Gender:", value['gender'])
        print("Year:", value['year'])
        print("Info:")

        for item in value['info']:

            if 'tag' in item:
                print("\tTag:", item['tag'])
            else:
                print("\tTag: [-1]")
        
        print()



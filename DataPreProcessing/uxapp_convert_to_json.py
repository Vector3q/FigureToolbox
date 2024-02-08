import json
import utils

def convert_to_json(feedback_text):
    user_feedback_lines = feedback_text.strip().split('\n')

    all_user_feedback = []
    
    count = 1
    count_id = 1
    current_user_feedback = None
    for line in user_feedback_lines:
        if line.startswith("User"):
            if current_user_feedback is not None:
                count = count + 1
                all_user_feedback.append(current_user_feedback)
            
            current_user_feedback = {"P"+str(count): {"gender":gender[count-1], "name":name[count-1], "year":year[count-1], "info":[]} }
            # current_user_feedback["P"+str(count)]["info"] = 
            count_id = 1
            print(current_user_feedback)
        else:
            if line.startswith("time"):
                current_user_feedback["P"+str(count)]["info"].append({"id":count_id, "status": 0 , "time": utils.time_to_seconds(line.split(": ")[-1].strip())})
                count_id = count_id+1
            elif line.startswith("tag"):
                current_user_feedback["P"+str(count)]["info"][-1]["tag"] = utils.tag_to_index(line.split(": ")[-1].strip())
            elif line.startswith("second_tag"):
                index_double = utils.second_tag_to_index(line.split(": ")[-1].strip())
                temp = {(str)(index_double[0]): [index_double[1]] }
                current_user_feedback["P"+str(count)]["info"][-1]["second_tag"] = temp

            elif line.startswith("description"):
                current_user_feedback["P"+str(count)]["info"][-1]["description"] = line.split(": ")[-1].strip()
            elif line.startswith("user_said"):
                current_user_feedback["P"+str(count)]["info"][-1]["user_said"] = line.split(": ")[-1].strip()
            elif line.startswith("reason"):
                current_user_feedback["P"+str(count)]["info"][-1]["reason"] = line.split(": ")[-1].strip()

    if current_user_feedback is not None:
        all_user_feedback.append(current_user_feedback)

    json_data = json.dumps(all_user_feedback, indent=2, ensure_ascii=False)
    
    return json_data


name = ['FL','XJA','XLN','ZSM','ZZY','WZY','LJW','LSJ','WXY','XZY']
gender = ['女','男','女','女','女','男','男','女','女','男'] 
year = ['23','22','27','27','24','25','21','27','28','24']
# 从文件中读取文本
file_path = "E:\Project\Gits\FigureToolbox\FigureToolbox\DataPreProcessing\chatgpt.txt"  # 替换为你的文件路径
with open(file_path, 'r', encoding='utf-8') as file:
    feedback_text = file.read()

# 调用函数并打印结果
json_result = convert_to_json(feedback_text)
print(json_result)

output_file_path = "E:\Project\Gits\FigureToolbox\FigureToolbox\DataPreProcessing\processedData.json"  # 替换为你的输出文件路径
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(json_result)

print(f"\nJSON 结果已成功写入到文件: {output_file_path}")
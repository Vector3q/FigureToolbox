def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def tag_to_index(str):
    if(str == "功能性问题"):
        return [1]
    elif(str == "系统反馈和错误处理"):
        return [2]
    elif(str == "导航和工作流程问题"):
        return [3]
    elif(str == "用户界面和体验问题"):
        return [4]
    elif(str == "性能和响应性"):
        return [5]
    elif(str == "无障碍和包容性问题"):
        return [6]
    elif(str == "帮助和文档"):
        return [7]
    elif(str == "自定义和灵活性"):
        return [8]
    elif(str == "AI理解和生成"):
        return [9]
    else:
        return [-1]

def second_tag_to_index(str):
    if(str == "文本编辑问题"):
        return [1,1]
    elif(str == "图像编辑问题"):
        return [1,2]
    elif(str == "功能完整性"):
        return [1,3]
    elif(str == "资产可用性"):
        return [1,4]
    elif(str == "错误信息的清晰度"):
        return [2,1]
    elif(str == "操作反馈"):
        return [2,2]
    elif(str == "过程清晰度"):
        return [3,1]
    elif(str == "步骤恢复"):
        return [3,2]
    elif(str == "元素选择"):
        return [4,1]
    elif(str == "选项和工具的可见性"):
        return [4,2]
    elif(str == "满意度"):
        return [4,3]
    elif(str == "系统速度"):
        return [5,1]
    elif(str == "系统可靠性"):
        return [5,2]
    elif(str == "语言和本地化"):
        return [6,1]
    elif(str == "无障碍功能"):
        return [6,2]
    elif(str == "教学支持"):
        return [7,1]
    elif(str == "用于详细任务的辅助功能"):
        return [7,2]
    elif(str == "帮助内容的可访问性"):
        return [7,3]
    elif(str == "布局和设计的适应性"):
        return [8,1]
    elif(str == "美学定制"):
        return [8,2]
    elif(str == "模板定制"):
        return [8,3]
    elif(str == "AI解释提示"):
        return [9,1]
    elif(str == "元素整合和一致性"):
        return [9,2]
    elif(str == "真实程度和风格匹配"):
        return [9,3]
    else:
        return [-1]
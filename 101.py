# 使用json模块解析输入并处理JSON数据
import json

def map_list_dict(input_dict, input_list):
    # 在这里编写你的代码
    target_dict = {}
    sub_dict = {}
    index = 0
    for element in input_dict:
        sub_dict[element] = input_dict[element]
        target_dict[input_list[index]] = sub_dict
        sub_dict = {}
        index += 1
    return target_dict

# 获取输入字符串并将其解析为json
input_dict = json.loads(input())
# 获取整数输入并将其转换为列表
input_list = list(map(int, input().split()))
# 调用函数
print(map_list_dict(input_dict, input_list))
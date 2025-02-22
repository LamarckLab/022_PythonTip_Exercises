def dict_to_sorted_list(dictionary):
    # 此处编写你的代码
    key_list = []
    target_list = []
    for element in dictionary:
        key_list.append(element)
    key_list = sorted(key_list)
    for element in key_list:
        target_list.append([element,dictionary[element]])
    return target_list
    # 获取输入转为字典
dictionary = eval(input())

# 调用函数 
print(dict_to_sorted_list(dictionary))
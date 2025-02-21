def get_sorted_keys_values(dict_obj):
    # 此处写你的代码
    key_list = []
    for element in dict_obj:
        key_list.append(element)
    sorted_list = sorted(key_list)
    value_list = []
    for element in sorted_list:
        value_list.append(dict_obj[element])
    return [sorted_list,value_list]

# 获取用户输入转为字典
dictionary = eval(input())

# 调用函数
print(get_sorted_keys_values(dictionary))
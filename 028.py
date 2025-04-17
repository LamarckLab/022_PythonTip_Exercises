def get_sorted_keys_values(dict_obj):
    # 此处写你的代码
    key_list = []
    value_list = []
    for item in dict_obj:
        key_list.append(item)
    key_list = sorted(key_list)
    for item in key_list:
        value_list.append(dict_obj[item])
    return [key_list,value_list]

# 获取用户输入转为字典
dictionary = eval(input())

# 调用函数
print(get_sorted_keys_values(dictionary))

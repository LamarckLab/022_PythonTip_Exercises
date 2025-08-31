def get_sorted_keys_values(dict_obj):
    # 此处写你的代码
    key_list = sorted(dict_obj)
    value_list = []
    for key in key_list:
        value_list.append(dict_obj[key])
    return [key_list,value_list]
# 获取用户输入转为字典
dictionary = eval(input())

# 调用函数
print(get_sorted_keys_values(dictionary))

def filter_dict_values(mixed_dict, k):
    # 此处写下你的代码
    target_dict = {}
    for element in mixed_dict:
        if type(mixed_dict[element]) == str:
            target_dict[element] = mixed_dict[element]
        else:
            if mixed_dict[element] > k:
                target_dict[element] = mixed_dict[element]
    return target_dict

# 获取输入 
user_dict = eval(input())
user_k = int(input())

# 调用函数 
print(filter_dict_values(user_dict, user_k))
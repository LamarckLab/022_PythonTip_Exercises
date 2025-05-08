def filter_dict_values(mixed_dict, k):
    # 此处写下你的代码
    output_dict  = {}
    for key in mixed_dict:
        if (type(mixed_dict[key]) == int and mixed_dict[key] > k) or type(mixed_dict[key]) != int:
            output_dict[key] = mixed_dict[key]
    return output_dict
# 获取输入 
user_dict = eval(input())
user_k = int(input())

# 调用函数 
print(filter_dict_values(user_dict, user_k))

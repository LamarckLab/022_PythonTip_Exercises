def remove_keys(dict_input, key_list):
    # 此处编写代码
    for element in key_list:
        dict_input.pop(element)
    return dict_input
# 获取输入 
user_dict = eval(input())
user_key_list = input().split()

# 调用函数 
print(remove_keys(user_dict, user_key_list))

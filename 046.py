def dict_to_sorted_list(dictionary):
    # 此处编写你的代码
    key_lst = []
    output_lst = []
    for key in dictionary:
        key_lst.append(key)
    for element in sorted(key_lst):
        output_lst.append([element,dictionary[element]])
    return output_lst

# 获取输入转为字典
dictionary = eval(input())

# 调用函数 
print(dict_to_sorted_list(dictionary))

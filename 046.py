def dict_to_sorted_list(dictionary):
    # 此处编写你的代码
    output_list = []
    for key in sorted(dictionary):
        sublist = [key, dictionary[key]]
        output_list.append(sublist)
    return output_list
# 获取输入转为字典
dictionary = eval(input())

# 调用函数 
print(dict_to_sorted_list(dictionary))

def swap_dict(dict):
    # 此处编写代码
    output_dict = {}
    for key in dict:
        if dict[key] not in output_dict:
            output_dict[dict[key]] = [key]
        else:
            output_dict[dict[key]] += [key]
    return output_dict
# 读取输入的字典 
dict = eval(input())

# 调用函数 
print(swap_dict(dict))

def swap_dict(dict):
    # 此处编写代码
    target_dict = {}
    for element in dict:
        if dict[element] not in target_dict:
            target_dict[dict[element]] = [element]
        else:
            target_dict[dict[element]] += [element]
    return target_dict

# 读取输入的字典 
dict = eval(input())

# 调用函数 
print(swap_dict(dict))
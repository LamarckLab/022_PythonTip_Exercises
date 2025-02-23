def count_frequency(lst):
    # 此处编写代码
    target_dict = {}
    for element in lst:
        if element not in target_dict:
            target_dict[element] = 1
        else:
            target_dict[element] += 1
    return target_dict

# 获取用户输入 
lst = list(input().split())

# 调用函数 
print(count_frequency(lst))
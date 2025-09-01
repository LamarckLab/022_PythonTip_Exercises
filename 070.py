def count_frequency(lst):
    # 此处编写代码
    frequency_dict = {}
    for word in lst:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1
    return frequency_dict 
# 获取用户输入 
lst = list(input().split())

# 调用函数 
print(count_frequency(lst))

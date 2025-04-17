def find_unique(lst):
    # 此处编写代码
    my_dict = {}
    for item in lst:
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] += 1
    output_lst = []
    for item in my_dict:
        if my_dict[item] == 1:
            output_lst.append(item)
    return output_lst

# 获取用户输入并转为数字列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique(numbers))

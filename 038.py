def find_unique(lst):
    # 此处编写代码
    cnt_dict = {}
    unique_list = []
    for element in lst:
        if element not in cnt_dict:
            cnt_dict[element] = 1
        else:
            cnt_dict[element] += 1
    for element in cnt_dict:
        if cnt_dict[element] == 1:
            unique_list.append(element)
    return unique_list

# 获取用户输入并转为数字列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique(numbers))
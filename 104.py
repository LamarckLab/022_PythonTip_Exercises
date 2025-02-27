def length_of_missing_list(list_of_lists):
    # 此处编写代码
    len_lst = []
    for element in list_of_lists:
        len_lst += [len(element)]
    min_len = min(len_lst)
    max_len = max(len_lst)
    len_sum = 0
    ideal_sum = 0
    for i in range(min_len,max_len+1):
        ideal_sum += i
    for j in len_lst:
        len_sum += j
    if ideal_sum == len_sum:
        return None
    else:
        return ideal_sum - len_sum

# 从用户输入中获取list_of_lists
list_of_lists = eval(input())
# 调用函数
print(length_of_missing_list(list_of_lists))
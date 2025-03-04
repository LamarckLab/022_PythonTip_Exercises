def replace_with_next_largest(num_list):
    # 此处编写代码
    sorted_lst = sorted(num_list)
    target_lst = []
    for element in num_list:
        index = sorted_lst.index(element)
        if index == len(num_list) - 1:
            target_lst += [-1]
        else:
            target_lst += [sorted_lst[index+1]]
    return target_lst
# 将输入的整数转换为列表
num_list = list(map(int, input().split()))
# 调用函数
print(replace_with_next_largest(num_list))
def max_gap(lst):
    # 此处编写代码
    max_gap = 0
    sorted_lst = sorted(lst)
    for index in range(len(lst)-1):
        max_gap = max(max_gap, sorted_lst[index+1] - sorted_lst[index])
    return max_gap
# 获取用户输入，转换为整数列表
numbers = list(map(int, input().split()))
# 调用函数，输出结果
print(max_gap(numbers))

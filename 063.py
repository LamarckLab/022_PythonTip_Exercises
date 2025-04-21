def max_gap(lst):
    # 此处编写代码
    max_gap = 0
    lst = sorted(lst)
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] > max_gap:
            max_gap = lst[i+1] - lst[i]
    return max_gap


# 获取用户输入，转换为整数列表
numbers = list(map(int, input().split()))
# 调用函数，输出结果
print(max_gap(numbers))

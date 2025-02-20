def difference_max_min(list_nums):
    # 在此处编写代码
    max_num = max(list_nums)
    min_num = min(list_nums)
    return max_num - min_num

# 输入整数，并将其转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(difference_max_min(numbers))
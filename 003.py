def difference_max_min(list_nums):
    # 在此处编写代码
    return max(list_nums) - min(list_nums)

# 输入整数，并将其转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(difference_max_min(numbers))

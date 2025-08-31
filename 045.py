def sum_missing_numbers(nums):
    # 此处编写代码
    min_num, max_num = min(nums), max(nums)
    lack_sum = 0
    for digit in range(min_num, max_num+1):
        if digit not in nums:
            lack_sum += digit
    return lack_sum
# 获取输入转为数字列表 
nums = list(map(int, input().split()))

# 调用函数 
print(sum_missing_numbers(nums))

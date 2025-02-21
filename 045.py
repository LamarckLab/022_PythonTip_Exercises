def sum_missing_numbers(nums):
    # 此处编写代码 
    max_num = max(nums)
    min_num = min(nums)
    target_sum = 0
    for element in range(min_num, max_num+1):
      if element not in nums:
        target_sum += element
    return target_sum

# 获取输入转为数字列表 
nums = list(map(int, input().split()))

# 调用函数 
print(sum_missing_numbers(nums))
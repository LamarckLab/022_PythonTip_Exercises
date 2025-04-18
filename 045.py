def sum_missing_numbers(nums):
    # 此处编写代码
    output_sum = 0
    for element in range(min(nums)+1, max(nums)):
        if element not in nums:
            output_sum += element
    return output_sum

# 获取输入转为数字列表 
nums = list(map(int, input().split()))

# 调用函数 
print(sum_missing_numbers(nums))

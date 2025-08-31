def is_consecutive_sequence(num_list):
    # 此处编写你的代码
    min_num, max_num = min(num_list), max(num_list)
    for digit in range(min_num, max_num+1):
        if digit not in num_list:
            return False
    return True
# 获取输入转为整数列表 
nums = list(map(int, input().split()))

# 调用函数 
print(is_consecutive_sequence(nums))

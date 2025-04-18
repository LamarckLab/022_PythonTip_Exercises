def is_consecutive_sequence(num_list):
    # 此处编写你的代码
    num_list = sorted(num_list)
    flag = True
    for index in range(0, len(num_list)-1):
        if num_list[index+1] - num_list[index] != 1:
            flag = False
    return flag


# 获取输入转为整数列表 
nums = list(map(int, input().split()))

# 调用函数 
print(is_consecutive_sequence(nums))

def count_consecutive_ones(input_list):
    # 此处编写代码 
    target_count = 0
    continue_count = 0
    for digit in input_list:
        if digit == 1:
            continue_count += 1
        else:
            if continue_count > 1:
                target_count += 1
            continue_count = 0
    if continue_count > 1:
        target_count += 1
    return target_count
# 获取输入, 转换为列表 
input_list = list(map(int, input().split()))
# 调用函数
print(count_consecutive_ones(input_list))
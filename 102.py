def count_consecutive_ones(input_list):
    # 此处编写代码
    target_count = 0
    continue_one = 0
    index = 0
    while index < len(input_list):
        if input_list[index] == 1:
            while input_list[index] == 1:
                continue_one += 1
                if index < len(input_list) - 1:
                    index += 1
                else:
                    if continue_one > 1:
                        target_count += 1
                    return target_count
            if continue_one > 1:
                target_count += 1
                continue_one = 0
                index += 1
            else:
                continue_one = 0
                index += 1
        else:
            index += 1
    return target_count


# 获取输入, 转换为列表 
input_list = list(map(int, input().split()))
# 调用函数
print(count_consecutive_ones(input_list))
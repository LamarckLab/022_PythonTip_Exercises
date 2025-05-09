def missing_numbers_info(num_list):
    # 此处写下你的代码
    sorted_list = sorted(num_list)
    start, end = sorted_list[0], sorted_list[-1]
    output_list = [0,0]
    for num in range(start, end+1):
        if num not in num_list:
            output_list[0] += 1
            output_list[1] += num
    return tuple(output_list)

# 获取整数输入并将其转换为列表
num_list = list(map(int, input().split()))
# 调用函数
print(missing_numbers_info(num_list))

def missing_numbers_info(num_list):
    # 此处写下你的代码
    max_num = max(num_list)
    min_num = min(num_list)
    target_lst = []
    sum_num = 0
    for digit in range(min_num,max_num+1):
        if digit not in num_list:
            target_lst += [digit]
            sum_num += digit
    return (len(target_lst), sum_num)

# 获取整数输入并将其转换为列表
num_list = list(map(int, input().split()))
# 调用函数
print(missing_numbers_info(num_list))
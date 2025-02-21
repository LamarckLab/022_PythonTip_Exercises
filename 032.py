def find_highest_number(numbers_list):
    # 此处编写代码 
    max_num = 0
    for element in numbers_list:
        max_num = max(max_num, element)
    return max_num


# 输入数字并转为列表
numbers_list = list(map(int, input().split()))

# 调用函数打印结果
print(find_highest_number(numbers_list))